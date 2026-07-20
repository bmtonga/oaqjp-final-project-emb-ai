# Task 3b - Formatted Output Test Results

## Terminal Output from Running Unit Tests

The following output was captured by running the test suite for the `emotion_detector` function using Python's `unittest` framework:

```
test_emotion_detector_anger
(test_emotion_detection.TestEmotionDetection.test_emotion_detector_anger)
Test that the statement 'I am really mad about this' returns 'anger' as
dominant emotion. ... ok
test_emotion_detector_disgust
(test_emotion_detection.TestEmotionDetection.test_emotion_detector_disgust)
Test that the statement 'I feel disgusted just hearing about this' returns
'disgust' as dominant emotion. ... ok
test_emotion_detector_fear
(test_emotion_detection.TestEmotionDetection.test_emotion_detector_fear)
Test that the statement 'I am really afraid that this will happen' returns
'fear' as dominant emotion. ... ok
test_emotion_detector_joy
(test_emotion_detection.TestEmotionDetection.test_emotion_detector_joy)
Test that the statement 'I am glad this happened' returns 'joy' as dominant
emotion. ... ok
test_emotion_detector_sadness
(test_emotion_detection.TestEmotionDetection.test_emotion_detector_sadness)
Test that the statement 'I am so sad about this' returns 'sadness' as
dominant emotion. ... ok
----------------------------------------------------------------------
Ran 5 tests in 0.006s
OK
```

## Test Summary

| Test Name | Input Statement | Expected Dominant Emotion | Result |
|-----------|----------------|--------------------------|--------|
| `test_emotion_detector_joy` | "I am glad this happened" | `joy` | ✅ Passed |
| `test_emotion_detector_anger` | "I am really mad about this" | `anger` | ✅ Passed |
| `test_emotion_detector_disgust` | "I feel disgusted just hearing about this" | `disgust` | ✅ Passed |
| `test_emotion_detector_sadness` | "I am so sad about this" | `sadness` | ✅ Passed |
| `test_emotion_detector_fear` | "I am really afraid that this will happen" | `fear` | ✅ Passed |

## Verification

- **Total Tests Run**: 5
- **Tests Passed**: 5
- **Tests Failed**: 0
- **Execution Time**: 0.006s

All tests confirm that the `emotion_detector` function correctly identifies the dominant emotion for each test statement, validating the output format as specified in Task 3a.
