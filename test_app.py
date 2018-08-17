from app import app, Question

import unittest

import json

class QuestionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.question_1 = Question('Held up?')
        self.question_2 = Question('Held up?')
    
    def test_get_all_questions(self):
        res = self.app.get('/api/v1.0/items')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.get_data(as_text=True))
        self.assertEqual(len(data['questions']), 2)


if __name__ == '__main__':
    unittest.main()
    