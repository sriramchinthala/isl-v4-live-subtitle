import os
import json
from pathlib import Path
from contextlib import asynccontextmanager

import numpy as np
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path.cwd()

MODEL_FILE = BASE_DIR / "best_landmark_model_v4.keras"
CLASS_FILE = BASE_DIR / "landmark_classes_v4.json"
WEB_FILE = BASE_DIR / "web" / "index.html"


# ============================================================
# SETTINGS
# ============================================================

SEQUENCE_LENGTH = 30
FEATURES = 126


# ============================================================
# GLOBAL STATE
# ============================================================

model = None
classes = []


# ============================================================
# LOAD MODEL
# ============================================================

def load_model():

    global model
    global classes

    if not MODEL_FILE.exists():

        raise FileNotFoundError(
            "Missing V4 model:\n"
            + str(MODEL_FILE)
        )

    if not CLASS_FILE.exists():

        raise FileNotFoundError(
            "Missing class file:\n"
            + str(CLASS_FILE)
        )

    import tensorflow as tf

    with open(
        CLASS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        classes = json.load(file)

    if not isinstance(classes, list):

        raise RuntimeError(
            "Invalid class file."
        )

    if len(classes) == 0:

        raise RuntimeError(
            "Class file is empty."
        )

    model = tf.keras.models.load_model(
        MODEL_FILE
    )

    print(
        "V4 model loaded successfully."
    )

    print(
        "Classes loaded:",
        len(classes)
    )


# ============================================================
# FASTAPI LIFESPAN
# ============================================================

@asynccontextmanager
async def lifespan(app):

    print("=" * 70)
    print("ISL V4 WEB SERVER")
    print("=" * 70)

    load_model()

    if WEB_FILE.exists():

        print(
            "Web frontend found:"
        )

        print(
            str(WEB_FILE)
        )

    else:

        print(
            "WARNING: web/index.html not found."
        )

    print("=" * 70)

    yield

    print(
        "ISL V4 web server stopped."
    )


# ============================================================
# APP
# ============================================================

app = FastAPI(
    title="ISL V4 Live Subtitle Server",
    version="1.0.0",
    lifespan=lifespan
)


# ============================================================
# HOME
# ============================================================

@app.get("/")
async def home():

    if not WEB_FILE.exists():

        return {
            "status": "error",
            "message":
                "web/index.html not found"
        }

    return FileResponse(
        str(WEB_FILE),
        media_type="text/html"
    )



# ============================================================
# VIDEO CALL PAGE
# ============================================================

CALL_FILE = BASE_DIR / "web" / "call.html"


@app.get("/call")
async def call_page():

    if not CALL_FILE.exists():

        return {
            "status": "error",
            "message": "web/call.html not found"
        }

    return FileResponse(
        str(CALL_FILE),
        media_type="text/html"
    )

# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "model_loaded":
            model is not None,
        "class_count":
            len(classes),
        "classes":
            classes,
        "frontend_exists":
            WEB_FILE.exists()
    }


# ============================================================
# PREDICTION
# ============================================================

def predict_sequence(sequence):

    if model is None:

        raise RuntimeError(
            "V4 model is not loaded."
        )

    sequence = np.asarray(
        sequence,
        dtype=np.float32
    )

    expected_shape = (
        SEQUENCE_LENGTH,
        FEATURES
    )

    if sequence.shape != expected_shape:

        raise ValueError(
            "Invalid sequence shape. "
            + "Expected "
            + str(expected_shape)
            + ", got "
            + str(sequence.shape)
        )

    max_value = np.max(
        np.abs(sequence)
    )

    if max_value > 0:

        sequence = (
            sequence / max_value
        )

    sequence = np.expand_dims(
        sequence,
        axis=0
    )

    prediction = model.predict(
        sequence,
        verbose=0
    )[0]

    indices = np.argsort(
        prediction
    )[::-1]

    results = []

    for index in indices[:5]:

        index = int(index)

        results.append(
            {
                "label":
                    classes[index],

                "confidence":
                    float(
                        prediction[index]
                    )
            }
        )

    return results


# ============================================================
# WEBSOCKET
# ============================================================

@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket
):

    await websocket.accept()

    print(
        "WebSocket client connected."
    )

    try:

        while True:

            message = await (
                websocket.receive_json()
            )

            message_type = message.get(
                "type"
            )


            # ------------------------------------------------
            # PING
            # ------------------------------------------------

            if message_type == "ping":

                await websocket.send_json(
                    {
                        "type": "pong"
                    }
                )

                continue


            # ------------------------------------------------
            # STATUS
            # ------------------------------------------------

            if message_type == "status":

                await websocket.send_json(
                    {
                        "type": "status",
                        "model_loaded":
                            model is not None,
                        "classes":
                            classes
                    }
                )

                continue


            # ------------------------------------------------
            # PREDICT
            # ------------------------------------------------

            if message_type == "predict":

                sequence = message.get(
                    "sequence"
                )

                if sequence is None:

                    await websocket.send_json(
                        {
                            "type":
                                "error",

                            "message":
                                "Missing sequence."
                        }
                    )

                    continue

                try:

                    results = (
                        predict_sequence(
                            sequence
                        )
                    )

                    await websocket.send_json(
                        {
                            "type":
                                "prediction",

                            "results":
                                results
                        }
                    )

                except Exception as error:

                    print(
                        "Prediction error:",
                        error
                    )

                    await websocket.send_json(
                        {
                            "type":
                                "error",

                            "message":
                                str(error)
                        }
                    )

                continue


            # ------------------------------------------------
            # UNKNOWN
            # ------------------------------------------------

            await websocket.send_json(
                {
                    "type":
                        "error",

                    "message":
                        "Unknown message type."
                }
            )


    except WebSocketDisconnect:

        print(
            "WebSocket client disconnected."
        )

    except Exception as error:

        print(
            "WebSocket error:",
            error
        )