from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from mserver import api

    app.register_blueprint(api.bp)
    return app
