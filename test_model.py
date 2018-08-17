import unittest

from app import Question

class QuestionTest(unittest.TestCase):

    def setUp(self):
        self.question1 = Question('what is osmosis?')
        self.question2 = Question('What is SSt?')

    def test_get_all_questions(self):
        self.assertEqual(len(Question._get_all_questions()), 2)
    
    def test_get_question_byId(self):
        result = Question._get_question_byId(2)
        self.assertEqual(result[0]['id'], 2)

if __name__ == '__main__':
    unittest.main()