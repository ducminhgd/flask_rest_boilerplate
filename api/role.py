from flask_restplus import Namespace, Resource

ns = Namespace('role', description='Role')

@ns.route('/')
class Roles(Resource):
    """Role operations"""

    def get(self):
        return 'Hello'
