"""
Mock emotion detection module for local testing.
Simulates the Watson NLP EmotionPredict API behavior.
"""

import re


def emotion_detector(text_to_analyze):
    """
    Function to run emotion detection using keyword-based analysis.
    
    Args:
        text_to_analyze (str): The text to be analyzed for emotions.
    
    Returns:
        dict: A dictionary containing emotion scores for anger, disgust, fear,
              joy, and sadness, along with the dominant emotion.
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    text_lower = text_to_analyze.lower()

    # Define keyword sets for each emotion with weights
    anger_keywords = ['angry', 'mad', 'furious', 'rage', 'outraged', 'hate', 'annoyed', 'irritated']
    disgust_keywords = ['disgusted', 'disgusting', 'gross', 'repulsive', 'revolting', 'sickening']
    fear_keywords = ['afraid', 'scared', 'fearful', 'terrified', 'anxious', 'worried', 'nervous', 'frightened']
    joy_keywords = ['happy', 'glad', 'joyful', 'delighted', 'pleased', 'enjoying', 'wonderful', 'fun', 'great', 'excellent', 'amazing', 'love']
    sadness_keywords = ['sad', 'sadness', 'unhappy', 'depressed', 'miserable', 'gloomy', 'heartbroken', 'crying', 'lonely']

    # Count occurrences with weighted scores
    def score_keywords(text, keywords):
        score = 0
        for keyword in keywords:
            count = len(re.findall(r'\b' + re.escape(keyword) + r'\w*', text))
            score += count * 0.15
        return min(score, 0.95)  # Cap at 0.95

    anger_score = score_keywords(text_lower, anger_keywords)
    disgust_score = score_keywords(text_lower, disgust_keywords)
    fear_score = score_keywords(text_lower, fear_keywords)
    joy_score = score_keywords(text_lower, joy_keywords)
    sadness_score = score_keywords(text_lower, sadness_keywords)

    # If no keywords matched, provide a baseline neutral analysis based on text length
    total_score = anger_score + disgust_score + fear_score + joy_score + sadness_score
    if total_score < 0.01:
        # Default small values to simulate API behavior
        anger_score = 0.05
        disgust_score = 0.03
        fear_score = 0.04
        joy_score = 0.06
        sadness_score = 0.02

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
