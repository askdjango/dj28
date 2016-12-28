from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size']
    list_display_links = ['id', 'title']

    def content_size(self, post):
        return '{}글자'.format(len(post.content))


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
