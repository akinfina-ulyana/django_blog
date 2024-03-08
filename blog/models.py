from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""
Конкретно-прикладной менеджер модели. 
Например, чтобы извлекать все статьи со статусом PUBLISHED
Можно добавлять дополнительные методы
менеджера в существующий менеджер либо создавать новый менеджер, ви-
доизменив изначальный набор запросов QuerySet, возвращаемый менедже-
ром.
"""
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
        # get_queryset() менеджера возвращает набор запросов QuerySet, переопределилa этот метод


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

