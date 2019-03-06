import settings

from flask import Flask
from flask_restplus import Api
from app.api.role import ns


def create_app():
    from app.commands import init_command
    from app.models import init_db

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=settings.SECRET_KEY,
        SQLALCHEMY_BINDS=settings.SQLALCHEMY_BINDS,
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
    )

    api = Api(app, version='1.0', title='Flask REST API')
    api.add_namespace(ns)

    init_db(app)
    init_command(app)

    return app
