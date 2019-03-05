from flask_restplus import Api
from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix=None)

api = Api(
    app=api_bp,
    version='1.0',
    title='Flask REST API Boilerplate',
    validate=False,
)

