import unittest
import json

from stats.app import start
from flask_testing import TestCase
 
class TestHelper(TestCase): # pragma: no cover
    def create_app(self):
        self.app = start(test=True)
        self.context = self.app.app_context()
        self.client = self.app.test_client()
        return self.app

    def tearDown(self):
        self.app = None
        self.context = None
        self.client = None
    
    def test_unknown_user(self):
        reply = self.client.get('/stats/400')  # Unknown user_id
        self.assertEqual(reply.status_code, 404)

    def test_known_user(self):
        reply = self.client.get('/stats/1')  # Known user_id
        self.assertEqual(reply.status_code, 200)
        result = json.loads(reply.data)
        self.assertEqual(result, {'score': 10.0})

