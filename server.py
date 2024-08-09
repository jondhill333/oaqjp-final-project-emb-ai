"""
This module implements a Flask server for emotion detection.

It provides routes for rendering the index page and performing emotion detection on text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Jons Assignment")

@app.route('/')
def render_index_page():
    """Render the index page of the application."""
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion() :
    """
    Detect emotions in the provided text.

    This function analyzes the text provided in the 'textToAnalyze' query parameter
    and returns a string describing the detected emotions and the dominant emotion.

    Returns:
        str: A formatted string containing the emotion analysis results,
             or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['anger']:
        return f"""For the given statement, the system response is 'anger': {result['anger']},
        'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}
        and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."""

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
