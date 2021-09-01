from rest_framework import viewsets
from rest_framework.response import Response


from .models import Blogs
from .serializers import BlogsSerializer

class BlogViewSet(viewsets.ViewSet):
    def list(self, request):  #/api/products
        blogs = Blogs.objects.all()
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)

    def create(self, request):  #/api/products
        pass

    def retrieve(self, request, pk=None): #/api/products/<str:id>
        pass

    def update(self, request, pk=None):
        pass

    def delete(self, request, pk=None):
        pass