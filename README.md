# Emotion Detection Application

A Flask-based web application that uses IBM Watson NLP EmotionPredict API to analyze text and detect emotions (anger, disgust, fear, joy, sadness) along with the dominant emotion.

## Project Structure

```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py              # Package initializer
│   └── emotion_detection.py     # Core emotion detection function
├── static/
│   └── mywebscript.js           # Frontend JavaScript
├── templates/
│   └── index.html               # Main web interface
├── server.py                    # Flask application server
├── test_emotion_detection.py    # Unit tests
├── setup.py                     # Package setup
├── README.md                    # Project documentation
└── LICENSE                      # License file
```

## Prerequisites

- Python 3.14+
- pip (Python package installer)

## Installation

1. Navigate to the project directory:
   
```bash
   cd oaqjp-final-project-emb-ai
   
```

2. Install required dependencies:
   
```bash
   pip install flask requests
   
```

## Running the Application

Start the Flask server:
```bash
python server.py
```

The application will be available at **http://localhost:5000**

## Usage

### Web Interface

1. Open http://localhost:5000 in your browser
2. Enter text in the input field
3. Click the analyze button to detect emotions

### API Endpoint

**Endpoint:** `GET /emotionDetector`

**Parameters:**
- `textToAnalyze` (required): The text to analyze for emotions

**Example Request:**
```
GET /emotionDetector?textToAnalyze=I am glad this happened
```

**Example Response:**
```
For the given statement, the system response is 'anger': 0.006, 'disgust': 0.002, 'fear': 0.009, 'joy': 0.95 and 'sadness': 0.008. The dominant emotion is joy.
```

**Error Handling:**
- Blank entries return HTTP 400 with message: `Invalid text! Please try again!`

## Running Tests

Execute the unit tests:
```bash
python test_emotion_detection.py
```

All 5 tests should pass:
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.006s

OK
```

The tests use mocked API responses, so no external network connection is required.

## Code Quality

Static code analysis with PyLint:
```bash
pip install pylint
python -m pylint server.py
```

Current score: **10.00/10**

## Core Function

The `emotion_detector()` function in `EmotionDetection/emotion_detection.py`:
- Accepts a text string as input
- Sends a POST request to the Watson NLP EmotionPredict API
- Returns a dictionary with emotion scores and the dominant emotion
- Returns `None` values for all keys when a blank entry is detected (HTTP 400)

## Technologies Used

- **Flask** - Web framework
- **IBM Watson NLP** - Emotion detection API
- **Python** - Programming language
- **unittest** - Testing framework
- **PyLint** - Static code analysis
