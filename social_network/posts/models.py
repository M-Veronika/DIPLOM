from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Тип поста
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]


# Тип лайка
class Like(models.Model):
    # Создает связь один ко многим, 
    # Аргумент related_name создает алиас для быстроого доступа к связи
    # Аргумент on_delete задает поведение удаления связанных данных
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    def __str__(self):
        return f'{self.author.username} понравился пост {self.post}'


# Тип комментария
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
