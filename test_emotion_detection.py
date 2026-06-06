from EmotionDetection import emotion_detector

# Test for joy
result = emotion_detector("I am glad this happened")
assert result["dominant_emotion"] == "joy"

# Test for anger
result = emotion_detector("I am really mad about this")
assert result["dominant_emotion"] == "anger"

# Test for disgust
result = emotion_detector("I feel disgusted just hearing about this")
assert result["dominant_emotion"] == "disgust"

# Test for sadness
result = emotion_detector("I am so sad about this")
assert result["dominant_emotion"] == "sadness"

# Test for fear
result = emotion_detector("I am really afraid that this will happen")
assert result["dominant_emotion"] == "fear"

print("All tests passed!")