from django.contrib import admin

from article.models import Comment, Category, Article

admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Article)
