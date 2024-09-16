import requests

def emotion_detector(text_to_analyze: str) -> str:
    """
    Send a POST to Emotion Predict function of the Watson NLP Library with the given text
    """

    # URL of the Emotion Predict Service
    url: str = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API request
    header: dict = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create a dictionary with the text to be analyzed
    input_text: json = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=input_text, headers=header, timeout=10)

    # return the text of the response
    return response.text