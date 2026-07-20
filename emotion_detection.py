import requests
import json


def emotion_detector(text_to_analyze):
    """
    Function to run emotion detection using Watson NLP EmotionPredict API.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        dict: A dictionary containing emotion scores for anger, disgust, fear,
              joy, and sadness, along with the dominant emotion.
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send request to Watson NLP EmotionPredict API
    response = requests.post(
        url,
        headers=headers,
        json=input_data
    )

    # Check for HTTP 400 Bad Request
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Convert response JSON into dictionary
    response_dict = json.loads(response.text)

    # Extract emotion predictions
    emotion_predictions = response_dict.get("emotionPredictions", [])

    if emotion_predictions:
        emotions = emotion_predictions[0].get("emotion", {})
    else:
        emotions = {}

    # Extract emotion scores
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)

    # Store scores in dictionary
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    # Find dominant emotion
    dominant_emotion = max(
        emotion_scores,
        key=emotion_scores.get
    )

    # Return final result
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }