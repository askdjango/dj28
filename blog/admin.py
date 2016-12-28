from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published', 'content_size', 'detail']
    list_display_links = ['id', 'title']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('comment_set')

    def content_size(self, post):
        return '{}글자'.format(len(post.content))

    def detail(self, post):
        id_list = ','.join(
            str(comment.id)
            for comment in post.comment_set.all())
        return 'comment id list : {}'.format(id_list)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
