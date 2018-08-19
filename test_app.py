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
        self.assertEqual(len(data['questions']), 1)

    def test_get_question_byId(self):
        res = self.app.get('/api/v2/questions/1')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.get_data(as_text=True))
        self.assertEqual(data['question'][0]['id'], 1)

    def test_add_question(self):
        result = {'name' : 'reality'}
        res = self.app.post('/api/v3/questions', data=result)
        self.assertEqual(res.status_code, 201)

    def test_add_answer(self):
        question2 = Question()
        question2._add_question('neuro science')
        result = question2._get_question_byId(1)
        pd = result[0]
        res = self.app.post('/api/v4/questions/1', data=pd)
        self.assertEqual(res.status_code, 201)

if __name__ == '__main__':
    unittest.main()
    