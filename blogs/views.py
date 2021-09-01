from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from .models import Blogs
from .serializers import BlogsSerializer

class BlogViewSet(viewsets.ViewSet):
    def list(self, request):  #/api/products
        blogs = Blogs.objects.all()
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)

    def create(self, request):  #/api/blogs
        serializer = BlogsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def retrieve(self, request, pk=None): #/api/products/<str:id>
        blog = Blogs.objects.gets(id=pk)
        serializer = BlogsSerializer(blog)
        return Response(serializer.data)

    def update(self, request, pk=None):
        blog = Blogs.objects.get(id=pk)
        serializer = BlogsSerializer(instance=blog, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def delete(self, request, pk=None):
        blog = Blogs.objects.get(id=pk)
        blog.delete()
        return Response(status=HTTP_204_NO_CONTENT)