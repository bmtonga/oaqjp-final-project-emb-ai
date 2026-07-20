import json
import unittest
from unittest.mock import patch
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Test class for the emotion_detector function.
    Uses mocked API responses to test emotion detection without external dependencies.
    """

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_joy(self, mock_post):
        """
        Test that the statement 'I am glad this happened' returns 'joy' as dominant emotion.
        """
        # Mock API response where joy has the highest score
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
        mock_post.return_value.json.return_value = mock_response
        mock_post.return_value.text = json.dumps(mock_response)
        mock_post.return_value.status_code = 200

        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
        self.assertGreater(result['joy'], result['anger'])
        self.assertGreater(result['joy'], result['disgust'])
        self.assertGreater(result['joy'], result['fear'])
        self.assertGreater(result['joy'], result['sadness'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_anger(self, mock_post):
        """
        Test that the statement 'I am really mad about this' returns 'anger' as dominant emotion.
        """
        # Mock API response where anger has the highest score
        mock_response = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.92,
                        "disgust": 0.02,
                        "fear": 0.01,
                        "joy": 0.005,
                        "sadness": 0.01
                    }
                }
            ]
        }
        mock_post.return_value.json.return_value = mock_response
        mock_post.return_value.text = json.dumps(mock_response)
        mock_post.return_value.status_code = 200

        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
        self.assertGreater(result['anger'], result['disgust'])
        self.assertGreater(result['anger'], result['fear'])
        self.assertGreater(result['anger'], result['joy'])
        self.assertGreater(result['anger'], result['sadness'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_disgust(self, mock_post):
        """
        Test that the statement 'I feel disgusted just hearing about this' returns 'disgust' as dominant emotion.
        """
        # Mock API response where disgust has the highest score
        mock_response = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.02,
                        "disgust": 0.89,
                        "fear": 0.01,
                        "joy": 0.005,
                        "sadness": 0.01
                    }
                }
            ]
        }
        mock_post.return_value.json.return_value = mock_response
        mock_post.return_value.text = json.dumps(mock_response)
        mock_post.return_value.status_code = 200

        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        self.assertGreater(result['disgust'], result['anger'])
        self.assertGreater(result['disgust'], result['fear'])
        self.assertGreater(result['disgust'], result['joy'])
        self.assertGreater(result['disgust'], result['sadness'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_sadness(self, mock_post):
        """
        Test that the statement 'I am so sad about this' returns 'sadness' as dominant emotion.
        """
        # Mock API response where sadness has the highest score
        mock_response = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.005,
                        "fear": 0.02,
                        "joy": 0.008,
                        "sadness": 0.91
                    }
                }
            ]
        }
        mock_post.return_value.json.return_value = mock_response
        mock_post.return_value.text = json.dumps(mock_response)
        mock_post.return_value.status_code = 200

        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        self.assertGreater(result['sadness'], result['anger'])
        self.assertGreater(result['sadness'], result['disgust'])
        self.assertGreater(result['sadness'], result['fear'])
        self.assertGreater(result['sadness'], result['joy'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_fear(self, mock_post):
        """
        Test that the statement 'I am really afraid that this will happen' returns 'fear' as dominant emotion.
        """
        # Mock API response where fear has the highest score
        mock_response = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.005,
                        "fear": 0.93,
                        "joy": 0.008,
                        "sadness": 0.02
                    }
                }
            ]
        }
        mock_post.return_value.json.return_value = mock_response
        mock_post.return_value.text = json.dumps(mock_response)
        mock_post.return_value.status_code = 200

        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')
        self.assertGreater(result['fear'], result['anger'])
        self.assertGreater(result['fear'], result['disgust'])
        self.assertGreater(result['fear'], result['joy'])
        self.assertGreater(result['fear'], result['sadness'])


if __name__ == '__main__':
    unittest.main()
