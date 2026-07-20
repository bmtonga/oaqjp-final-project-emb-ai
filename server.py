"""
Flask server for Emotion Detection application.
Provides a web interface to analyze text and detect emotions.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the main page of the Emotion Detection application.
    """
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Analyze the provided text and return the emotion detection results.
    
    Expects a GET parameter 'textToAnalyze' containing the text to analyze.
    Returns a formatted string with emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    # Format the response as specified
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
