from rest_framework import serializers
from blog.models import Post, Comment
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class ListPostSerializer(serializers.ModelSerializer):
    author = UserSerializers(required=True)
    comment_count = serializers.IntegerField()
    """All about posts"""

    class Meta:
        model = Post
        fields = (
            "title",
            "author",
            "creation_date",
            "comment_count",
        )


class PostSerializer(serializers.ModelSerializer):
    """Serializer for create, read, delete and update post"""

    class Meta:
        model = Post
        fields = ("title", "link", "creation_date", "author")


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for create, read, delete and update comment"""

    class Meta:
        model = Comment
        fields = ("author", "content", "post")


class UpvoteSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField()
    """Serializer for count upvote"""

    class Meta:
        model = Post
        fields = (
            "title",
            "upvote_count",
        )

    def get_upvote_count(self, obj):
        return obj.upvote.count()


class ToUpvoteSerializer(serializers.ModelSerializer):
    """Serializer for to upvote the post"""

    class Meta:
        model = Post
        fields = ("upvote",)
