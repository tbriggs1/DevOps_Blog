from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.Charfield(max_length=200)
    description = models.Charfield(max_length=20000)
    image = models.Charfield(max_length=2000)


class User(models.Model):
    pass