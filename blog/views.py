from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

def post_list(request): # обязательный объект, содержащтй информацию о запросе
    posts = Post.published.all()  # достаём все опубликованные посты
    return render(request, 'blog/post/list.html', {'posts': posts})
    # render() - функция сокращенного доступа, «охватывает» несколько уровней MVC


def post_detail(request, year, month, day, post): # представление детальной информации о посте (опубликованном)
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})












