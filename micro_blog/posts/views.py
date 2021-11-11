from django.core import paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Post, Group, User, Follow
from .forms import PostForm, CommentForm

def _get_posts(request, filter_: dict):
    post_list = Post.objects.filter(**filter_).prefetch_related(
        'author',
        'group',
        'comments',
    ).all()

    #TODO delete paginator var after tests
    paginator = Paginator(post_list, 10)
    page = paginator.get_page(request.GET.get('page'))
    return page

def _read_author(username):
    author = get_object_or_404(User, username=username)
    post_cout = Post.objects.filter(
        author=author
    ).count()

    follow_count = Follow.objects.filter(
        author=author
    ).count()

    self_follow_count = Follow.objects.filter(
        user=author
    ).count()

    return author, post_cout, follow_count, self_follow_count

def _read_post(request, post_id):
    post = Post.objects.filter(id=post_id).select_related(
        'author',
        'group'
    ).prefetch_related('comments').last()

    author, count_post, follow_count, self_follow_count = _read_author(
        post.author.username
    )

    form = CommentForm(request.POST or None)
    all_comments = post.comments.select_related('author').all().order_by('-created')
    return {
        'author': author,
        'post': post,
        'count_post': count_post,
        'form': form,
        'comments': all_comments,
        'profile': author,
        'follow_count': follow_count,
        'self_follow_count': self_follow_count,        
    }