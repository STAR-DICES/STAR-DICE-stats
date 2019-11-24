import requests

from jsonschema import validate, ValidationError
from flask import request, jsonify, abort
from flakon import SwaggerBlueprint


stats = SwaggerBlueprint('stats', 'stats', swagger_spec='stats-specs.yaml')

"""
This endpoint returns the stats for the specified user
"""
@stats.operation('stats')
def _stats(writer_id, user_id):
    # Maybe not needed.
    if not general_validator('stats', user_id):
        abort(400)

    # TODO: we should make the user_id parameter optional, if missing return only the published stories.
    r = requests.get(stories_url + "/stories-by-writer?writer_id=" + str(user_id) + "&user_id=" + str(user_id+1))
    if r.status_code != 200:
        abort(404)

    stories = json.loads(r.json())
    return jsonify({'score': compute_score(stories)})

def general_validator(op_id, request):
    schema = follows.spec['paths']
    for endpoint in schema.keys():
        for method in schema[endpoint].keys():
            if schema[endpoint][method]['operationId'] != op_id:
                continue

            op_schema = schema[endpoint][method]['parameters'][0]
            if 'schema' not in op_schema:
                return True

            definition= op_schema['schema']['$ref'].split("/")[2]
            schema= follows.spec['definitions'][definition]
            try:
                validate(request.get_json(), schema=schema)
            except ValidationError as error:
                return False
            return True

"""
This function returns the score of the user taking the sum of all likes received over the number of dislikes,
divided by the number of published stories.
"""
def compute_score(stories):
    tot_stories = 0
    tot_likes = 0
    tot_dislikes = 0
    for story in stories:
        tot_stories += 1
        tot_likes += story.likes
        tot_dislikes += story.dislikes
    if tot_stories == 0:
        return 0
    if tot_likes == 0:
        tot_likes = 1
    if tot_dislikes == 0:
        tot_dislikes = 1
    return round((tot_likes / tot_dislikes) / tot_stories, 2)
