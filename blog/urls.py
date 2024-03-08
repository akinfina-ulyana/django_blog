from django.urls import path
from . import views

app_name = 'blog'
""" определяет именное пространство; упoрядочивает URL-адреса по приложениям, при обращении к ним использует имя
    in html: blog:post_detail
"""

urlpatterns = [
# представления поста
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]