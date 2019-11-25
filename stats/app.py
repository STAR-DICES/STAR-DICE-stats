import datetime
import json
import os

from stats.views import blueprints
from stats.request import real_request, test_request

from flakon import create_app
from swagger_ui import api_doc


request = None

def start(test = False):
    app = create_app(blueprints=blueprints)
    if test:
        app.config['TESTING'] = True
        request = test_request
    else:
        request = real_request
    api_doc(app, config_path='stats-specs.yaml', url_prefix='/api', title='API doc')
    return app

if __name__ == '__main__':
    app = start()
    app.run()
