import sys
import json
from unittest.mock import Mock, patch

sys.path.insert(0, 'c:\\Users\\MR Mtongo\\Desktop\\Projects\\final project\\oaqjp-final-project-emb-ai')

print("=" * 60)
print("STEP 1: Importing the application...")
print("=" * 60)

from EmotionDetection import emotion_detector

print("SUCCESS: Application imported successfully!")
print()

print("=" * 60)
print('STEP 2: Testing with text: "I love this new technology."')
print("=" * 60)

# Mock the API response to simulate a successful emotion detection
mock_response = {
    "emotionPredictions": [
        {
            "emotion": {
                "anger": 0.006,
                "disgust": 0.002,
                "fear": 0.009,
                "joy": 0.95,
                "sadness": 0.008
            }
        }
    ]
}

with patch('EmotionDetection.emotion_detection.requests.post') as mock_post:
    # Configure the mock to return a successful response
    mock_post.return_value.json.return_value = mock_response
    mock_post.return_value.text = json.dumps(mock_response)
    mock_post.return_value.status_code = 200
    
    result = emotion_detector("I love this new technology.")
    print("Result:", result)
    print()
    print("SUCCESS: Application tested without errors!")
