# ISL V4 Live Subtitle

A real-time Indian Sign Language (ISL) recognition web application that uses a webcam to detect hand landmarks, classify signs with a TensorFlow V4 model, and convert recognized signs into live English subtitles.

## Live Demo

**Live Application:**
https://isl-v4-live-subtitle.onrender.com

**GitHub Repository:**
https://github.com/sriramchinthala/isl-v4-live-subtitle

## Project Overview

ISL V4 Live Subtitle is designed to recognize selected Indian Sign Language gestures through a webcam and display the corresponding English words and simple sentences in real time.

The application combines:

* Browser webcam access
* MediaPipe Hands
* 126-dimensional hand-landmark features
* TensorFlow/Keras V4 classification model
* FastAPI backend
* WebSocket communication
* Live English sentence generation
* Public HTTPS deployment using Render

## Main Features

### Real-Time Camera Recognition

The application accesses the user's webcam directly from the browser and processes the video stream in real time.

### Hand Landmark Detection

MediaPipe Hands detects hand landmarks from each camera frame.

The application uses:

* 21 landmarks per hand
* X, Y and Z coordinates
* 63 features per hand
* 126 features for two hands

### V4 Sign Recognition Model

The backend loads:

`best_landmark_model_v4.keras`

The model currently contains 10 supported sign classes.

### Supported Signs

The current V4 model includes:

* BAD
* FOOD
* GOOD
* HELP
* WATER
* WELCOME
* WHAT
* WHERE
* WHO
* YOU

### Live English Subtitle

Recognized signs are converted into English text.

Examples:

* `YOU + WATER` → **You want water?**
* `YOU + FOOD` → **You want food?**
* `YOU + HELP` → **Do you need help?**
* `YOU + WHERE` → **Where are you?**
* `YOU + WHO` → **Who are you?**
* `YOU + WHAT` → **What do you want?**

### Confidence Display

The web interface displays the model's prediction confidence percentage for the current recognition.

### Duplicate Suppression

The frontend uses stable-prediction logic and hand-release behavior to reduce repeated recognition of the same sign.

### Controls

The interface provides:

* Start Camera
* Pause / Resume
* Clear
* Undo

## System Architecture

```text
Webcam
   |
   v
Browser
   |
   v
MediaPipe Hands
   |
   v
Hand Landmark Extraction
   |
   v
126-Dimensional Feature Vector
   |
   v
30-Frame Sequence
   |
   v
WebSocket
   |
   v
FastAPI Server
   |
   v
TensorFlow V4 Model
   |
   v
Sign Prediction + Confidence
   |
   v
Sentence Builder
   |
   v
Live English Subtitle
```

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* WebRTC / `getUserMedia`
* MediaPipe Hands
* WebSocket client

### Backend

* Python
* FastAPI
* Uvicorn
* WebSocket
* NumPy

### Machine Learning

* TensorFlow
* Keras
* MediaPipe hand landmarks

### Deployment

* Git
* GitHub
* Render
* HTTPS
* Secure WebSocket support

## Project Structure

```text
NEW/
├── .python-version
├── .gitignore
├── requirements.txt
├── best_landmark_model_v4.keras
├── landmark_classes_v4.json
├── server_v1.py
└── web/
    └── index.html
```

## Backend API

### Home

```text
GET /
```

Returns the web application.

### Health Check

```text
GET /health
```

Returns backend status, model status and loaded classes.

### WebSocket

```text
/ws
```

The browser sends a 30-frame landmark sequence to the backend.

Prediction messages use:

```json
{
  "type": "predict",
  "sequence": [...]
}
```

The server returns the prediction results and confidence values.

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/sriramchinthala/isl-v4-live-subtitle.git
cd isl-v4-live-subtitle
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Start the server

```powershell
python -m uvicorn server_v1:app --host 127.0.0.1 --port 8000
```

### 5. Open the application

```text
http://127.0.0.1:8000
```

Allow camera access when the browser asks for permission.

## Deployment

The application is deployed as a Python Web Service on Render.

### Build Command

```text
pip install -r requirements.txt
```

### Start Command

```text
uvicorn server_v1:app --host 0.0.0.0 --port $PORT
```

### Python Version

```text
3.13
```

The TensorFlow version used by the project is:

```text
2.21.0
```

## How Recognition Works

The browser captures webcam frames and passes them through MediaPipe Hands.

The landmark coordinates are organized into a 126-dimensional vector:

```text
Left hand  = 63 values
Right hand = 63 values
Total      = 126 values
```

A sequence of 30 frames is collected before sending the sequence to the backend.

The TensorFlow V4 model returns the most likely sign class and its confidence.

The frontend then:

1. Stabilizes the prediction.
2. Prevents immediate duplicate acceptance.
3. Adds the recognized word.
4. Builds a simple English sentence.
5. Displays the result as a live subtitle.

## Example

Input:

```text
YOU
WATER
```

Output:

```text
You want water?
```

Input:

```text
YOU
FOOD
```

Output:

```text
You want food?
```

## Current Limitations

The current system is a prototype focused on a selected set of ISL signs rather than complete Indian Sign Language coverage.

The sentence builder currently uses predefined sentence patterns and does not perform full natural-language understanding.

Recognition accuracy can be affected by:

* Lighting conditions
* Camera quality
* Hand position
* Background clutter
* Signer variation
* Occlusion
* Fast hand movement

The current model recognizes the trained sign classes only.

## Future Scope

Future versions can include:

* More ISL signs
* Larger and more diverse datasets
* Improved two-hand recognition
* Continuous sentence recognition
* Better grammar correction
* Natural-language generation
* Voice output
* Mobile application support
* User-specific adaptation
* Better duplicate suppression
* Improved low-light performance
* Offline deployment
* GPU acceleration
* More robust sentence understanding

## Project Goal

The long-term goal is to develop an accessible real-time communication system that can help bridge communication between Indian Sign Language users and people who do not understand sign language.

## Status

**Current Status: Working**

* Local web application: ✅
* Camera recognition: ✅
* MediaPipe hand tracking: ✅
* V4 TensorFlow model: ✅
* WebSocket backend: ✅
* Live English subtitles: ✅
* GitHub repository: ✅
* Public Render deployment: ✅

## Author

**Sriram**

Indian Sign Language Live Subtitle — V4
