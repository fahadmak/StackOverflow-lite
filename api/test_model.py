from model import Questions

import unittest

class QuestionTestCase(unittest.TestCase):

    def setUp(self):
        self.qn = Questions('the bad man?')
                    
    def test_get_all_questions(self):  
        self.assertEqual(1, len(Questions.questions))

    def test_get_all_questions_returns_error_message_if_there_are_no_questions(self):
        Questions.questions = []
        self.assertRaises(ValueError, Questions.get_all_questions(Questions.questions), [])    

if __name__ == '__main__':
    unittest.main()
    
