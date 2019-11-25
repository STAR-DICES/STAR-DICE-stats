import requests
import json


stories_url = '127.0.0.1:6000'  # TODO: insert real stories microservice url

class Request:
    def __init__(self, get_stories, timeout=1):
        self._get_stories = get_stories
        self._timeout = timeout

    def get_stories(self, author_id):
        return self._get_stories(author_id, self._timeout)

class TestResponse:
    def __init__(self, status_code, response_data):
        self.status_code = status_code
        self._json = json.dumps(response_data)

    def json(self):
        return self._json


existing_response = {
    'stories': [{
        'story_id': 1,
        'title': 'Spooky',
        'text': 'The green zombie waves at the green ghost.',
        'rolls_outcome': ['zombie', 'ghost', 'green', 'goo'],
        'theme': "Halloween",
        'date': '10/10/1010',
        'likes': 10,
        'dislikes': 1,
        'published': True,
        'author_id': 1,
        'author_name': 'Admin'
        }
    ]
}

def test_get_stories(author_id, timeout):
    if author_id == 1:
        return TestResponse(200, existing_response)
    return TestResponse(404, None)

def real_get_stories(author_id, timeout):
    return requests.get(stories_url + "/stories?writer_id=" + str(author_id), timeout=timeout)


test_request = Request(test_get_stories)
real_request = Request(real_get_stories)
