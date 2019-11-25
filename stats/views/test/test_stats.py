import unittest
import json

from stats.app import start


class TestStats(unittest.TestCase):
    def setUp(self):
        self.app = start(test=True)
        self.context = self.app.app_context()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app = None
        self.context = None
        self.client = None
    
    def test_unknown_user(self):
        reply = self.client.get('/stats/400')  # Unknown user_id
        self.assertEqual(reply.status_code, 404)

    def test_known_user(self):
        reply = self.client.get('/stats/1')  # Known user_id
        print(reply)
        self.assertEqual(reply.status_code, 200)
        #data = reply.json()
        #self.assertEqual(data, json.dumps({'score': 10}))

