from common.configuration.db import db


class BlogModel(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.String(), primary_key=True)
    title = db.Column(db.String())
    blog_date = db.Column(db.String())
    description = db.Column(db.String())
    image = db.Column(db.String())

    def __init__(self, id, title, blog_date, description, image):
        self.id = id
        self.title = title
        self.blod_date = blog_date
        self.description = description
        self.image = image

    def __repr__(self):
        return f"<User {self.username}>"

    @classmethod
    def get_all_blogs(cls):
        return cls.query.all()