from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Post, Group, User, Follow
from .forms import PostForm, CommentForm

def _get_posts(request, filter_: dict):
    pass

def _read_author(username):
    pass

def _read_post(request, post_id):
    pass

def index(request):
    pass

def group_posts(request, slug):
    pass

def profile(request, username):
    pass

def post_view(request, username, post_id):
    pass

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