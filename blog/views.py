from django.shortcuts import render
from .models import Post
from django.http import Http404

def post_list(request): # обязательный объект, содержащтй информацию о запросе
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})
    # render() - функция сокращенного доступа, «охватывает» несколько уровней MVC


def post_detail(request, id): # представление детальной информации о посте
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})








