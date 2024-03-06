from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # поля отображения в админке
    list_filter = ['status', 'created', 'publish', 'author'] # фильтр правая панель
    search_fields = ['title', 'body'] # строка поиска, можно выпотнять по указанным полям
    prepopulated_fields = {'slug': ('title',)} # автоматическое заполнение для slug
    raw_id_fields = ['author'] # Виджет для отбора ассоциированных объектов (индекс пользователя, вместо имени)
    date_hierarchy = 'publish' # навигация по иерархии дат
    ordering = ['status', 'publish']
