from .models import Post, Comment
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Post

        fields =(
            'text',
            'group',
            'image',
        )

        lables = {
            'text': 'Текст статьи',
            'group': 'Выберите группу',
        }

        help_texts = {
            'text': 'Введите текст статьи',
            'group': 'Выберите группу',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        labels = {'text': 'Текст комментария'}
        help_texts = {'text': 'Введите текст комментария'}