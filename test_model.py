import unittest

from app import Question

class QuestionTest(unittest.TestCase):

    def test_get_all_questions(self):
        self.assertEqual(len(Question._get_all_questions()), 1)
    
    def test_get_question_byId(self):
        self.question2 = Question()
        result = Question._get_question_byId(1)
        self.assertEqual(result[0]['id'], 1)

    def test_add_question(self):
        self.question2 = Question()
        result = self.question2._add_question('neuro science')
        self.assertEqual(self.question2.question['name'], 'neuro science')
        self.assertEqual(self.question2.question['id'], 1)
    
if __name__ == '__main__':
    unittest.main()