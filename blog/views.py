from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, publish__year=year,
                             publish__month=month, publish__day=day, slug=slug)
    return render(request, 'blog/post/detail.html', {'post': post})
