from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Post, Group, User, Follow
from .forms import PostForm, CommentForm

POSTS_ON_PAGE_COUNT = 1

def _get_posts(request, filter_: dict):
    post_list = Post.objects.filter(**filter_).prefetch_related(
        'author',
        'group',
        'comments',
    ).all()
    paginator = Paginator(post_list, POSTS_ON_PAGE_COUNT)
    page = paginator.get_page(request.GET.get('page'))
    return page

def _read_author(username):
    author = get_object_or_404(User, username=username)
    post_count = Post.objects.filter(author=author).count()
    follow_count = Follow.objects.filter(
        author=author
    ).count()
    self_follow_count = Follow.objects.filter(
        user=author
    ).count()
    return author, post_count, follow_count, self_follow_count

def _read_post(request, post_id):
    pass

def index(request):
    page = _get_posts(request, {})
    return render(
        request,
        'index.html',
        {
            'page': page,
            'page_number': page.number
        }
    )

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    page = _get_posts(request, {'group': group})
    return render(
        request,
        'group.html',
        {
            'group': group,
            'page': page,
        }
    )

def profile(request, username):
    author, count_post, follow_count, self_follow_count = _read_author(username)
    page = _get_posts(
        request,
        {'author':author}
    )
    check_follow = Follow.objects.filter(
        user=request.user, author=author
    ).exists()
    return render(
        request,
        'profile.html',
        {
            'page': page,
            'author': author,
            'profile': author,
            'count_post': count_post,
            'following': check_follow,
            'follow_count': follow_count,
            'self_follow_count': self_follow_count,
        }
    )
def post_view(request, username, post_id):
    context = _read_post(request, post_id)
    return render(
        request,
        'post.html',
        context,
    )

def add_comment(request, username, post_id):
    pass

def new_post(request):
    pass

def post_edit(request, username, post_id):
    pass

def page_not_found(request, exception):
    pass

def server_error(request):
    pass

def follow_index(request):
    pass

def profile_follow(request, username):
    pass

def profile_unfollow(request, username):
    pass