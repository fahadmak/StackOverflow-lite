from app import app, Question

import unittest

import json

class QuestionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.question2 = Question()
        self.question2._add_question('what is your name?')
                    
    def test_get_all_questions(self):
        res = self.app.get('/api/v1/questions')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.get_data(as_text=True))
        self.assertEqual(len(data['questions']), 2)

    def test_get_question_byId(self):
        res = self.app.get('/api/v2/questions/1')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.get_data(as_text=True))
        self.assertEqual(data['question'][0]['id'], 1)

    def test_add_question(self):
        result = {'name' : 'reality'}
        res = self.app.post('/api/v3/questions', data=result)
        self.assertEqual(res.status_code, 201)

if __name__ == '__main__':
    unittest.main()
    