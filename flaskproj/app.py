import os
from flask import Flask

def create_app(test_Config = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
    SECRET_KEY='dev',
    Database = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    @app.route('/')
    def hello():
        return 'disaster web'

    return app
