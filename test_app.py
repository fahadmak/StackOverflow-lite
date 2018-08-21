from app.views import app
from flask import Flask

import unittest

import json

class QuestionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.question = {"qn_id": 3, "title" : "kkjddhdbdjddj", "body" : "njaahkhj kjkjhkjda a"}
        self.answer ={"qn_id": 3, "an_id" : 4, "descr" : "djddfasfsakfshsfkjfshsfkhf"}
                
    def test_get_all_questions(self):
        """Test StackOver FlowLite API can get all (GET request)."""
        response = self.app.get('/api/v1/questions')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['questions']), 2)
    
    def test_get_question_byId(self):
        """Test API can fetch a question by using it's id."""
        response = self.app.get('/api/v1/questions/1')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
    
    def test_add_question(self):
        """Test API can create a single question."""
        response = self.app.post('/api/v1/questions',
                                 data=json.dumps(self.question),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_add_answer(self):
        """Test API can create a single answer."""
        response = self.app.post('/api/v1/questions/1/answers',
                                 data=json.dumps(self.answer),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
    