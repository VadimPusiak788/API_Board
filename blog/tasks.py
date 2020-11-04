from celery import shared_task
from .models import Post


@shared_task()
def show():
    posts = Post.objects.all()

    for post in posts:
        post.total = 0
        post.save()
