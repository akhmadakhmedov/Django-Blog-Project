from django.contrib import admin

# Register your models here.
from .models import Article, Comment

admin.site.register(Comment)

@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display=["title", 'author', 'created_date']
    list_display_links=['title', 'created_date']
    list_filter = ['created_date']
    search_fields = ['title']
    class Meta:
        model = Article
