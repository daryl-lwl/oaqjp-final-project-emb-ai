""" To detect emotions of a given statement """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    """ Class for retrieving and to output the response."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again."
    various_emotions = str(response[:-1]).replace('{',' ')
    various_emotions = various_emotions.replace('(',' ')
    various_emotions = various_emotions.replace('}',' ')
    various_emotions = various_emotions.replace(')',' ')
    various_emotions = various_emotions[:-3]
    dominant_response = response[-1].split()
    return f"For the given statement, the system response is {various_emotions}. \
    The dominant emotion is {dominant_response[-1]}."

@app.route("/")
def render_index_page():
    """ Rendering template """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
