from rest_framework import serializers
from .models import Blogs


class BlogsSerializer(serializers.ModelSerializer):
    class meta:
        model = Blogs
        fields = '__all__'