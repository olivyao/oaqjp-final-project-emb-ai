"""
Flask emotion detection
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    render main page
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_analyzer():
    """
    Analyze the emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)
    #extract emotions
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']
    response = (
        f"For the given statement, the system response is "
        f"'anger':{anger}"
        f"'disgust':{disgust}"
        f"'fear':{fear}"
        f"'joy':{joy}"
        f"'sadness': {sadness}"
        f"'The dominant emotion is': {dominant}"
    )
    return response

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000, debug=True)
