from rest_framework import generics, permissions
from blog.models import Post, Comment
from .serializers import (
    ListPostSerializer,
    CommentSerializer,
    PostSerializer,
    UpvoteSerializer,
    ToUpvoteSerializer,
)
from django.db.models import Count


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.annotate(comment_count=Count("comments_post"))
    serializer_class = ListPostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvoteAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = UpvoteSerializer


class ToUpvoteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = ToUpvoteSerializer
