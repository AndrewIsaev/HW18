from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.movie import movie_ns


def create_app(config_obj):
    application = Flask(__name__)
    application.config.from_object(config_obj)
    configure_app(application)
    return application


def configure_app(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    # api.add_namespace()
    # api.add_namespace()


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(port=5000)
