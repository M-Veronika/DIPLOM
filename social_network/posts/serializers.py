from rest_framework import serializers
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['author', 'post']


# Сериализация поста

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    # Приведение лайков к их колличеству
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['likes_count'] = len(ret['likes'])
        ret.pop('likes')
        return ret

    class Meta:
        model = Post

        # Определение доступных полей
        fields = ['id', 'text', 'image', 'created_at', 'comments', 'likes']
