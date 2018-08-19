import unittest

from app import Question

class QuestionTest(unittest.TestCase):

    def test_get_all_questions(self):
        question2 = Question()
        self.assertEqual(len(Question._get_all_questions()), 2)
    
    def test_get_question_byId(self):
        question2 = Question()
        result = Question._get_question_byId(1)
        self.assertEqual(result[0]['id'], 1)

    def test_add_question(self):
        question2 = Question()
        result = question2._add_question('neuro science')
        self.assertEqual(question2.question['name'], 'neuro science')
        self.assertEqual(question2.question['id'], 2)

    def test_add_answer(self):
        
        question2 = Question()
        question2._add_question('neuro science')
        question2._add_answer(1, 'nemo')
        result = Question._get_question_byId(1)
        self.assertEqual(result[0]['answer'], 'nemo')
        
if __name__ == '__main__':
    unittest.main()