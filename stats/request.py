import requests
import json


class Request:
    def __init__(self, get_stories, timeout=1):
        self._get_stories = get_stories
        self._timeout = timeout

    def get_stories(self, author_id):
        return self._get_stories(author_id, self._timeout)

class Response:
    def __init__(self, status_code, response_data):
        self.status_code = status_code
        self._json = json.dumps(response_data)

    def json(self):
        return self._json


existing_response = {
    'stories': [{
        'story_id': 1,
        'title': 'Test title',
        'text': '',
        'rolls_outcome': ['zombie', 'ghost', 'green', 'goo'],
        'theme': "Halloween",
        'data': '10/10/1010',
        'likes': 10,
        'dislikes': 1,
        'published': True,
        'author_id': 1,
        'author_name': 'Admin'
        }
    ]
}

def test_get_stories(author_id, timeout):
    return Response(200, existing_response)
    if author_id == 1:
        return Response(200, existing_response)
    return Response(404, None)

def real_get_stories(author_id, timeout):
    return requests.get(stories_url + "/stories?writer_id=" + str(author_id), timeout=timeout)


test_request = Request(test_get_stories)
real_request = Request(real_get_stories)
