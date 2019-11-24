import json

from flask_testing import TestCase


class TestStats(TestCase):
    def create_app(self):
        self.app = create_app(test=True)
        self.context = self.app.app_context()
        self.client = self.app.test_client()
        return self.app

    def tearDown(self):
        pass
    
    def unknown_user(self):
        reply = self.client.get('/stats/400')  # Unknown user_id
        self.assertEqual(reply.status_code, 404)

    def known_user(self):
        reply = self.client.get('/stats/1')  # Known user_id
        self.assertEqual(reply.status_code, 200)
        data = json.loads(reply.get_json())
        self.assertEqual(data, {'score': 1})  # TODO: substiture real expected score

