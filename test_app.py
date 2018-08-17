from app import app, Question

import unittest

import json

class QuestionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
                    
    def test_get_all_questions(self):
        res = self.app.get('/api/v1/questions')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.get_data(as_text=True))
        self.assertEqual(len(data['questions']), 2)

    def test_get_question_byId(self):
        res = self.app.get('/api/v2/questions/2')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.get_data(as_text=True))
        self.assertEqual(data['question'][0]['id'], 2)
        

if __name__ == '__main__':
    unittest.main()
    