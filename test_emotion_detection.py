from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        result_1_split = result_1[-1].split()
        self.assertEqual(result_1_split[-1],'joy')
        
        result_2 = emotion_detector('I am really mad about this')
        result_2_split = result_2[-1].split()
        self.assertEqual(result_2_split[-1], 'anger')

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        result_3_split = result_3[-1].split()    
        self.assertEqual(result_3_split[-1], 'disgust')

        result_4 = emotion_detector('I am so sad about this')
        result_4_split = result_4[-1].split()    
        self.assertEqual(result_4_split[-1], 'sadness')

        result_5 = emotion_detector('I am really afraid that this will happen')
        result_5_split = result_5[-1].split()    
        self.assertEqual(result_5_split[-1], 'fear')

unittest.main()