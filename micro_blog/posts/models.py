from typing import Text
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import constraints
from django.db.models.fields.files import ImageField

User = get_user_model()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self) -> str:    
        # переопределение строкового метода для удобства тестирования
        # выводит только первые 20 символов текста статьи
        return self.text[:20]

class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    
    text = models.TextField()
    created = models.DateTimeField('Date published', auto_now_add=True)

    def __str__(self) -> str:
        return self.text

class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','author'],
                name='unique_follow'
            )
        ]

class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title