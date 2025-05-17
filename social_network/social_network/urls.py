"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import (
    PostListCreateView, PostDetailView,
    CommentListCreateView, CommentDetailView,
    LikeListCreateView
)
from django.conf import settings
from django.conf.urls.static import static

# Сопоставление путей и представлений
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path(
        'comments/',
        CommentListCreateView.as_view(),
        name='comment-list-create'
        ),
    path(
        'comments/<int:pk>/',
        CommentDetailView.as_view(),
        name='comment-detail'
        ),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create')
] \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)