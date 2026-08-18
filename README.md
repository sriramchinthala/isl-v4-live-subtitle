# ISL V4 Live Subtitle

A real-time Indian Sign Language (ISL) recognition and accessible video communication web application that uses a webcam to detect hand landmarks, classify signs with a TensorFlow V4 model, convert recognized signs into live English subtitles, and support voice-based communication between participants.

## Live Demo

**Main Video Call Application:**
https://isl-v4-live-subtitle.onrender.com/call

**Main Website:**
https://isl-v4-live-subtitle.onrender.com

**GitHub Repository:**
https://github.com/sriramchinthala/isl-v4-live-subtitle

## Project Overview

ISL V4 Live Subtitle is designed to recognize selected Indian Sign Language gestures through a webcam and convert the recognized signs into English words and simple sentences in real time.

The platform also provides accessible browser-based video communication between participants, allowing users to combine sign language, live subtitles, voice input, and text-to-speech communication.

The application combines:

* Browser webcam and microphone access
* MediaPipe Hands
* 126-dimensional hand-landmark features
* TensorFlow/Keras V4 classification model
* FastAPI backend
* WebSocket communication
<<<<<<< HEAD
* WebRTC / PeerJS video communication
=======
* WebRTC / browser video communication
>>>>>>> a197dd5 (Update README with main video call link)
* Live English sentence generation
* Voice-to-text communication
* Text-to-speech output
* Live conversation transcript
* Public HTTPS deployment using Render

## Main Features

### Accessible Video Calling

The main application provides browser-based video communication with:

* Real-time laptop ↔ phone video calling
* Browser camera and microphone support
* Room-based video calls
* Shareable room links
* Live ISL subtitles for the opposite participant
* Voice-to-text communication
* Text-to-speech for incoming messages
* Live transcript history
* Accessibility-focused controls

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

The backend loads the V4 landmark classification model.

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

Recognized signs are converted into English text and can be sent to the opposite participant during a video call.

Examples:

* `YOU + WATER` → **You want water?**
* `YOU + FOOD` → **You want food?**
* `YOU + HELP` → **Do you need help?**
* `YOU + WHERE` → **Where are you?**
* `YOU + WHO` → **Who are you?**
* `YOU + WHAT` → **What do you want?**

### Confidence Display

The web interface displays the model's prediction confidence for the current recognition.

### Duplicate Suppression

The frontend uses stable-prediction logic and hand-release behavior to reduce repeated recognition of the same sign.

### Voice-to-Text Communication
<<<<<<< HEAD

Users can speak through the browser microphone and convert speech into text.

The recognized text can be sent to the opposite participant during a video call.

### Text-to-Speech Communication

Incoming subtitle or voice text can be read aloud using browser speech synthesis.

### Live Transcript

The video-call interface can maintain a live conversation transcript containing recognized sign messages and voice messages.

### Signing Safe Area

The interface provides a visual signing guide that helps the signer keep the hands and upper body inside an appropriate camera region.

### Hand Landmark Visualization

The interface can display the detected hand skeleton and landmarks over the signer's camera feed.

### Studio Contrast Mode

The signer view can use enhanced contrast styling to improve hand and upper-body visibility.

### Mouse and Interaction Effects

The interface includes lightweight interaction effects designed to provide a more polished desktop experience without interfering with camera and AI processing.
=======

Users can speak through the browser microphone and convert speech into text.

The recognized text can be sent to the opposite participant during a video call.

### Text-to-Speech Communication

Incoming subtitle or voice text can be read aloud using browser speech synthesis.

### Live Transcript

The video-call interface can maintain a live conversation transcript containing recognized sign messages and voice messages.

### Signing Safe Area

The interface provides a visual signing guide that helps the signer keep the hands and upper body inside an appropriate camera region.

### Hand Landmark Visualization

The interface can display the detected hand skeleton and landmarks over the signer's camera feed.

### Studio Contrast Mode

The signer view can use enhanced contrast styling to improve hand and upper-body visibility.

### Mouse and Interaction Effects

The interface includes lightweight interaction effects designed to provide a more polished desktop experience without interfering with camera and AI processing.

### Controls

The interface provides accessible controls for:

* Create Room
* Join Room
* Camera control
* Hand skeleton display
* Signing guide
* Studio contrast mode
* Voice input
* Auto voice output
* Live transcript
* Hang up
>>>>>>> a197dd5 (Update README with main video call link)

## System Architecture

```text
                     ┌─────────────────────┐
                     │      Webcam         │
                     └──────────┬──────────┘
                                |
                                v
                     ┌─────────────────────┐
                     │ Browser Frontend    │
                     │ HTML/CSS/JavaScript │
                     └──────────┬──────────┘
                                |
                ┌───────────────┴────────────────┐
                |                                |
                v                                v
      ┌───────────────────┐            ┌───────────────────┐
      │ MediaPipe Hands   │            │ WebRTC / PeerJS   │
      └─────────┬─────────┘            └─────────┬─────────┘
                |                                |
                v                                v
      ┌───────────────────┐             Video + Data Channel
      │ Landmark          │                     |
      │ Extraction        │                     v
      └─────────┬─────────┘            Opposite Participant
                |
                v
      ┌───────────────────┐
      │ 126-Dimensional   │
      │ Feature Vector    │
      └─────────┬─────────┘
                |
                v
      ┌───────────────────┐
      │ 30-Frame Sequence │
      └─────────┬─────────┘
                |
                v
      ┌───────────────────┐
<<<<<<< HEAD
      │ WebSocket         │
=======
      │ WebSocket          │
>>>>>>> a197dd5 (Update README with main video call link)
      └─────────┬─────────┘
                |
                v
      ┌───────────────────┐
<<<<<<< HEAD
      │ FastAPI Server    │
=======
      │ FastAPI Server     │
>>>>>>> a197dd5 (Update README with main video call link)
      └─────────┬─────────┘
                |
                v
      ┌───────────────────┐
      │ TensorFlow V4     │
      │ Classification    │
      └─────────┬─────────┘
                |
                v
      ┌───────────────────┐
      │ Sign Prediction   │
      │ + Confidence      │
      └─────────┬─────────┘
                |
                v
      ┌───────────────────┐
      │ Sentence Builder  │
      └─────────┬─────────┘
                |
                v
      ┌───────────────────┐
      │ Live English      │
      │ Subtitle          │
      └─────────┬─────────┘
                |
                v
      Opposite Participant
```

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* WebRTC
* PeerJS
* `getUserMedia`
* MediaPipe Hands
* WebSocket client
* Browser Speech Recognition
* Browser Speech Synthesis

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
├── server_v1.py
├── best_landmark_model_v4.keras
├── landmark_classes_v4.json
└── web/
    ├── index.html
    └── call.html
```

## Backend API

### Home

```text
GET /
```

Returns the main web application.

### Health Check

```text
GET /health
```

Returns backend status, model status, and loaded classes.

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

The server returns prediction results and confidence values.

## Video Call Communication

The main video-call interface is available at:

```text
https://isl-v4-live-subtitle.onrender.com/call
```

The same application can be opened on both devices.

Typical flow:

```text
Laptop
  |
  | Create Room
  v
Room Code / Invite Link
  |
  v
Phone
  |
  | Join Room
  v
Video + Audio + Subtitle Communication
```

During a call:

```text
ISL Sign
   |
   v
AI Prediction
   |
   v
English Subtitle
   |
   v
Opposite Participant
```

Voice communication can also be used:

```text
Voice
   |
   v
Speech Recognition
   |
   v
Text
   |
   v
Opposite Participant
```

Incoming text can be converted to speech:

```text
Incoming Text
   |
   v
Browser Text-to-Speech
   |
   v
Audio Output
```

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

### 5. Open the main application

```text
http://127.0.0.1:8000
```

### 6. Open the video-call application

```text
http://127.0.0.1:8000/call
```

Allow camera and microphone access when the browser asks for permission.

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
6. Sends the subtitle to the opposite participant when connected.

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

Input:

```text
YOU
HELP
```

Output:

```text
Do you need help?
```

## Accessibility Design

The video-call interface is designed around accessible communication.

Key interface elements include:

* Large readable live captions
* High-contrast subtitle presentation
* Signing safe-zone guidance
* Optional hand skeleton overlay
* Studio contrast mode
* Voice-to-text input
* Text-to-speech output
* Live transcript history
* Simple room-based calling
* Responsive desktop and mobile layout

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

Browser support for speech recognition and speech synthesis can vary by device and browser.

The public deployment depends on browser permissions, network connectivity, and the availability of the deployed service.

## Future Scope

Future versions can include:

* More ISL signs
* Larger and more diverse datasets
* Improved two-hand recognition
* Continuous sentence recognition
* Better grammar correction
* Natural-language generation
* More advanced voice output
* Mobile application support
* User-specific adaptation
* Better duplicate suppression
* Improved low-light performance
* Offline deployment
* GPU acceleration
* More robust sentence understanding
* Expanded accessibility features

## Project Goal

The long-term goal is to develop an accessible real-time communication system that can help bridge communication between Indian Sign Language users and people who do not understand sign language.

The project combines sign-language recognition, live captioning, video communication, voice interaction, and text-to-speech into a single accessible communication platform.

## Status

**Current Status: Working**

* Local web application: ✅
* Camera recognition: ✅
* MediaPipe hand tracking: ✅
* V4 TensorFlow model: ✅
* WebSocket backend: ✅
* Live English subtitles: ✅
* Accessible video calling: ✅
* Voice-to-text communication: ✅
* Text-to-speech communication: ✅
* Live transcript: ✅
* GitHub repository: ✅
* Public Render deployment: ✅
* Main video-call application: ✅

## Public Links

**Main Video Call:**
https://isl-v4-live-subtitle.onrender.com/call

**Main Website:**
https://isl-v4-live-subtitle.onrender.com

**GitHub Repository:**
https://github.com/sriramchinthala/isl-v4-live-subtitle

## Author

**Sriram**

Indian Sign Language Live Subtitle — V4
