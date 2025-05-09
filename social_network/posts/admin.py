from django.contrib import admin

from .models import Post, Comment, Like


# Регистрация моделей в админке Django
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)

