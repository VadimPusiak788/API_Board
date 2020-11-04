from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post


@receiver(m2m_changed, sender=Post.upvote.through)
def upvote_count(sender, instance, **kwargs):
    instance.total = instance.upvote.count()
    instance.save()