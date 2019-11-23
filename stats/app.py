import datetime
import json
import os

from stats.views import blueprints

from flakon import create_app
from swagger_ui import api_doc


def start(test = False):
    app = create_app(blueprints=blueprints)
    if test:
        app.config['TESTING'] = True
    api_doc(app, config_path='follows-specs.yaml', url_prefix='/api', title='API doc')
    return app

if __name__ == '__main__':
    app = start()
    app.run()
