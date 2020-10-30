from django.urls import path
from .views import (
    PostAPIView,
    CommentAPIView,
    PostDetailAPIView,
    PostCreateAPIView,
    UpvoteAPIView,
    CommentDetailAPIView,
    ToUpvoteAPIView,
)


app_name = "api"

urlpatterns = [
    path("about_post/", PostAPIView.as_view()),
    path("post/", PostCreateAPIView.as_view()),
    path("post/<int:pk>/", PostDetailAPIView.as_view()),
    path("comment/", CommentAPIView.as_view()),
    path("comment/<int:pk>/", CommentDetailAPIView.as_view()),
    path("upvote/", UpvoteAPIView.as_view()),
    path("upvote/<int:pk>/", ToUpvoteAPIView.as_view()),
]
