from typing import Text
from django.db import models
from django.contrib.auth import get_user_model
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