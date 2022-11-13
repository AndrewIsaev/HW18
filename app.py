from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.movie import movie_ns


def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    configure_app(application)
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    # api.add_namespace()
    # api.add_namespace()


app_config = Config()
app = create_app(app_config)

if __name__ == '__main__':
    app.run()
