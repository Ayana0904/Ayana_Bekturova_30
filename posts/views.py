from django.shortcuts import render
from posts.models import Post


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context_data = {
            'list_of_post': posts
        }

        return render(request, 'posts/posts.html', context=context_data)


