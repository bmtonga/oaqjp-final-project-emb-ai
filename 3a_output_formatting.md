# Task 3a - Output Formatting of the Modified `emotion_detector` Function

## File Location

The modified `emotion_detector` function is located at:
`oaqjp-final-project-emb-ai/EmotionDetection/emotion_detection.py`

## Complete Modified Function Code

```python
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
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=input_data)

    # Check if the response status code indicates an error (blank entry)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert the response text into a dictionary
    response_dict = json.loads(response.text)

    # Extract the emotion scores from the response
    emotion_predictions = response_dict.get('emotionPredictions', [])
    if emotion_predictions:
        emotions = emotion_predictions[0].get('emotion', {})
    else:
        emotions = {}

    # Extract required emotions with their scores
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    # Find the dominant emotion (the one with the highest score)
    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(scores, key=scores.get)

    # Return the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
```

## Correct Output Format

The function returns a **Python dictionary** with the following key-value pairs:

### 1. Successful Analysis (Normal Response)

When a valid text is provided, the function returns:

```python
{
    'anger': <float>,          # Score for anger (e.g., 0.006)
    'disgust': <float>,        # Score for disgust (e.g., 0.002)
    'fear': <float>,           # Score for fear (e.g., 0.009)
    'joy': <float>,            # Score for joy (e.g., 0.95)
    'sadness': <float>,        # Score for sadness (e.g., 0.008)
    'dominant_emotion': <str>  # The emotion with the highest score (e.g., 'joy')
}
```

**Example 1: Joy as dominant emotion**

Input: `"I am glad this happened"`

Output:
```python
{
    'anger': 0.006,
    'disgust': 0.002,
    'fear': 0.009,
    'joy': 0.95,
    'sadness': 0.008,
    'dominant_emotion': 'joy'
}
```

**Example 2: Anger as dominant emotion**

Input: `"I am really mad about this"`

Output:
```python
{
    'anger': 0.92,
    'disgust': 0.02,
    'fear': 0.01,
    'joy': 0.005,
    'sadness': 0.01,
    'dominant_emotion': 'anger'
}
```

**Example 3: Disgust as dominant emotion**

Input: `"I feel disgusted just hearing about this"`

Output:
```python
{
    'anger': 0.02,
    'disgust': 0.89,
    'fear': 0.01,
    'joy': 0.005,
    'sadness': 0.01,
    'dominant_emotion': 'disgust'
}
```

**Example 4: Sadness as dominant emotion**

Input: `"I am so sad about this"`

Output:
```python
{
    'anger': 0.01,
    'disgust': 0.005,
    'fear': 0.02,
    'joy': 0.008,
    'sadness': 0.91,
    'dominant_emotion': 'sadness'
}
```

**Example 5: Fear as dominant emotion**

Input: `"I am really afraid that this will happen"`

Output:
```python
{
    'anger': 0.01,
    'disgust': 0.005,
    'fear': 0.93,
    'joy': 0.008,
    'sadness': 0.02,
    'dominant_emotion': 'fear'
}
```

### 2. Blank/Invalid Entry (Error Handling)

When an empty or blank text is provided (HTTP 400 status code), the function returns:

```python
{
    'anger': None,
    'disgust': None,
    'fear': None,
    'joy': None,
    'sadness': None,
    'dominant_emotion': None
}
```

## Summary of Key Modifications

This modified version includes the following enhancements over the original:

1. **400 Status Code Handling**: Added a check for `response.status_code == 400` to handle blank/empty text entries gracefully, returning `None` for all emotion scores and `dominant_emotion`.

2. **Correct Output Format**: Returns a structured dictionary with:
   - Five emotion scores (`anger`, `disgust`, `fear`, `joy`, `sadness`) as float values
   - One `dominant_emotion` key containing the string name of the emotion with the highest score

3. **Consistent Dictionary Structure**: All six keys are always present in the returned dictionary, making it predictable and easy to consume by the Flask server (`server.py`).
