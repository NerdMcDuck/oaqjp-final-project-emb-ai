import json

import requests


def emotion_detector(text_to_analyze: str) -> dict:
    """
    Send a POST to Emotion Predict function of the Watson NLP Library with the given text
    """

    # URL of the Emotion Predict Service
    url: str = (
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp"
        ".v1/NlpService/EmotionPredict"
    )

    # Set the headers required for the API request
    header: dict = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Create a dictionary with the text to be analyzed
    input_text: json = {"raw_document": {"text": text_to_analyze}}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=input_text, headers=header, timeout=10)

    # return the text of the response
    return _extract_emotions(response)


def _extract_emotions(response) -> dict:
    """
    Extract the required set of emotions along with their scores
    """

    # set all values to None when the staus_code is 400
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # Parsing the JSON response from the API
    json_response: json = json.loads(response.text)

    # Get the predictions
    emotion_predictions: list = json_response["emotionPredictions"]

    # Parse out the emotions dictionary
    emotions: dict = emotion_predictions[0]["emotion"]

    # Get the dominant emotion score
    dominant_emotion_score = max(list(emotions.values()))

    for emotion, score in emotions.items():
        if dominant_emotion_score == score:
            emotions["dominant_emotion"] = emotion
            break

    return emotions
