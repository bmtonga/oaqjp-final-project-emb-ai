# Unit Testing Results

## Test Execution Output

```
test_emotion_detector_anger (test_emotion_detection.TestEmotionDetection.test_emotion_detector_anger)
Test that the statement 'I am really mad about this' returns 'anger' as dominant emotion. ... ok
test_emotion_detector_disgust (test_emotion_detection.TestEmotionDetection.test_emotion_detector_disgust)
Test that the statement 'I feel disgusted just hearing about this' returns 'disgust' as dominant emotion. ... ok
test_emotion_detector_fear (test_emotion_detection.TestEmotionDetection.test_emotion_detector_fear)
Test that the statement 'I am really afraid that this will happen' returns 'fear' as dominant emotion. ... ok
test_emotion_detector_joy (test_emotion_detection.TestEmotionDetection.test_emotion_detector_joy)
Test that the statement 'I am glad this happened' returns 'joy' as dominant emotion. ... ok
test_emotion_detector_sadness (test_emotion_detection.TestEmotionDetection.test_emotion_detector_sadness)
Test that the statement 'I am so sad about this' returns 'sadness' as dominant emotion. ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.007s

OK
```

## Test Summary

| Test Method | Input Statement | Expected Dominant Emotion | Result |
|---|---|---|---|
| `test_emotion_detector_joy` | "I am glad this happened" | joy | ✅ Passed |
| `test_emotion_detector_anger` | "I am really mad about this" | anger | ✅ Passed |
| `test_emotion_detector_disgust` | "I feel disgusted just hearing about this" | disgust | ✅ Passed |
| `test_emotion_detector_sadness` | "I am so sad about this" | sadness | ✅ Passed |
| `test_emotion_detector_fear` | "I am really afraid that this will happen" | fear | ✅ Passed |

**All 5 unit tests passed successfully.**
