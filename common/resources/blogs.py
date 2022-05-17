from flask_restful import Resource
from common.models.blog import BlogModel
from flask_jwt import jwt_required

class Blogs(Resource):

    def get(self):

        response_body = {
            BlogModel.get_all_blogs()
        }

        return response_body
