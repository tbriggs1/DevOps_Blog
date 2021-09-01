from django.contrib import admin
from django.urls import path
from blogs.views import BlogViewSet, UserAPIView

urlpatterns = [
    path('blogs', BlogViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('blogs/<str:pk>', BlogViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'
    })),
    path('user', UserAPIView.as_view())
]
