from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
import os
from common.resources.blogs import Blogs
from common.resources.user_crud import User
from common.configuration.db import db
from common.resources.crop_crud import Blog
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://tbriggs:example@172.30.0.1:5436/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "supersecret"
db.init_app(app)

CORS(app)


jwt = JWT(app, authenticate, identity)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(User, "/user")
api.add_resource(Blogs, "/blogs")
api.add_resource(Blog, "/blog")


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
