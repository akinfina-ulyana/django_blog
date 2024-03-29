from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

"""
def post_list(request): # обязательный объект, содержащтй информацию о запросе
    post_list = Post.published.all() # достаём все опубликованные посты
    paginator = Paginator(post_list, 3)  # экземпляр класса Paginator, 3 поста на страницу
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page_number не целое число, то выдать первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если page_number находится вне диапазона, то выдать последнюю страницу
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})
    # render() - функция сокращенного доступа, «охватывает» несколько уровней MVC
"""

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


class PostListView(ListView):
    # Альтернативное представление списка постов

    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = 'blog/post/list.html'











