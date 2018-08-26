import unittest

from flask import json

from app.views import app

from tests.test_data import *


class QuestionsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_question_creation(self):
        """Test API can create a ride (POST request)"""
        response = self.app.post('api/v1/questions',
                                    content_type='application/json',
                                    data=json.dumps(post_question1))
        self.assertEqual(response.status_code, 201)
        self.assertIn("Question added", str(response.data))

    def test_answer_creation(self):
        """Test API can create a ride (POST request)"""
        q_response = self.app.post('api/v1/questions',
                                 content_type='application/json',
                                 data=json.dumps(post_question1))
        a_response = self.app.post('api/v1/questions/1/answers',
                                    content_type='application/json',
                                    data=json.dumps(post_answer1))

        self.assertEqual(a_response.status_code, 201)
        self.assertIn("Answer added", str(a_response.data))

    def test_api_can_get_all_questions(self):
        """Test RideAPI can view all (GET request)."""
        response2 = self.app.post('api/v1/questions',
                                 content_type='application/json',
                                 data=json.dumps(post_question1))
        self.assertEqual(response2.status_code, 201)
        response = self.app.get('api/v1/questions')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['questions']), 2)

    def test_api_can_get_question_by_id(self):
        """Test API can fetch a single question by using it's id."""
        # post data
        response = self.app.post('api/v1/questions',
                                    content_type='application/json',
                                    data=json.dumps(post_question1))
        self.assertEqual(response.status_code, 201)
        request = self.app.get('/api/v1/questions/1')
        data = json.loads(request.get_data())
        self.assertEqual(data['question'][-1]['qn_id'], 1)

    def test_api_can_get_error_if_title_is_integer(self):
        """Test API can get error if title is integer (POST request)"""
        response = self.app.post('api/v1/questions',
                                 content_type='application/json',
                                 data=json.dumps(post_question3))
        self.assertEqual(response.status_code, 400)

    def test_api_can_get_error_if_title__empty(self):
        """Test API can get error if title is empty (POST request)"""
        response = self.app.post('api/v1/questions',
                                 content_type='application/json',
                                 data=json.dumps(post_question4))
        self.assertEqual(response.status_code, 400)

    def test_api_can_get_error_if_body_empty(self):
        """Test API can get error if body is empty (POST request)"""
        response = self.app.post('api/v1/questions',
                                 content_type='application/json',
                                 data=json.dumps(post_question5))
        self.assertEqual(response.status_code, 400)

    def test_api_can_get_error_if_body_integer(self):
        """Test API can get error if body is integer (POST request)"""
        response = self.app.post('api/v1/questions',
                                 content_type='application/json',
                                 data=json.dumps(post_question6))
        self.assertEqual(response.status_code, 400)

    def test_api_can_get_error_if_id_string(self):
        """Test API can get error if id is string (POST request)"""
        response = self.app.post('api/v1/questions',
                                 content_type='application/json',
                                 data=json.dumps(post_question7))
        self.assertEqual(response.status_code, 400)

    def test_api_can_get_error_if_id_empty(self):
        """Test API can get error if id is string (POST request)"""
        response = self.app.post('api/v1/questions',
                                 content_type='application/json',
                                 data=json.dumps(post_question8))
        self.assertEqual(response.status_code, 400)

    def test_api_can_get_error_if_id_doesnt_exist(self):
        """Test API can get error if id is string (POST request)"""
        response = self.app.get('api/v1/questions/34')
        self.assertEqual(response.status_code, 404)

