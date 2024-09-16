"""
Server file for the flask application
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_app():
    """
    Takes the user input and sends it to emotion_detector
    """

    text_to_analyze: str = request.args.get("textToAnalyze")

    response: dict = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "<strong> Invalid text! Please try again! </strong>"

    formatted_output = (f"For the given statement, the system response is 'anger': "
                            f"{response['anger']}, 'disgust': {response['disgust']}, "
                            f"'fear': {response['fear']}, 'joy': {response['joy']}, and "
                            f"'sadness': {response['sadness']}. "
                            f"The dominant emotion is <b>{response['dominant_emotion']}. </b>")
    return formatted_output

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
