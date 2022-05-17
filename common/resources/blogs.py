from flask_restful import Resource
from common.models.blog import BlogModel
from flask_jwt import jwt_required

class Blogs(Resource):

    def get(self):
        return {'blogs': list(map(lambda x: x.json(), BlogModel.query.all()))}
