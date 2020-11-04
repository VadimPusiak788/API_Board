from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=256)
    link = models.URLField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvote = models.ManyToManyField(User, related_name="upvote_user", blank=True)
    total = models.PositiveIntegerField(db_index=True, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments_post"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment of {self.author.username}"
