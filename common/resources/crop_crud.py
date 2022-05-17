from flask_restful import Resource
from flask import request
from flask_jwt import jwt_required
from common.models.blog import BlogModel
from common.configuration.db import db
import uuid


class Blog(Resource):

    def get(self):
        data = request.args.get('id')
        print(data)
        print(type(data))
        blog = BlogModel.query.filter_by(id=data).first()
        result = {"title": blog.title, "description": blog.description,
                  "image": blog.image, "date": blog.blog_date}

        return {"blog": result}

    def post(self):
        if request.json:
            data = request.get_json()
            new_blog = BlogModel(
                id=str(uuid.uuid4()),
                title=data["title"],
                description=data["description"],
                image=data["image"],
                blog_date=data["blog_date"]
            )
            db.session.add(new_blog)
            db.session.commit()

            return {"Message": f"Blog {new_blog.title} has been created successfully"}

        return {"Error": "Unable to create blog"}

    def delete(self, id):
        blog = BlogModel.query.get_or_404(id)
        db.session.delete(blog)
        db.session.commit()
        return {"message": "blog deleted"}

    def put(self, id):
        blog = BlogModel.query.get_or_404(id)
        data = request.get_json()
        blog.title = data["title"]
        blog.description = data["description"]
        blog.image = data["image"]

        db.session.add(blog)
        db.session.commit()
        return {"message": "Successfully updated crop details"}
