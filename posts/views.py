from django.shortcuts import render, redirect, reverse
from elasticsearch_dsl import Search

from posts.models import Post


def home(request):
    search = Search(index="post_index")
    result = search.execute()
    data = result.hits
    return render(request, 'index.html', {'posts': data})


def create_post(request):
    return render(request, 'create.html')


def save_post(request):
    title = request.POST.get('title')
    body = request.POST.get('body')
    post = Post.objects.create(title=title, body=body)
    post.indexing()
    return redirect(reverse('posts:index'))
