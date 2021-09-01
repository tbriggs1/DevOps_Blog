#!/bin/bash

docker stop devops_blog_backend_1 devops_blog_db_1

git pull

docker-compose up -d