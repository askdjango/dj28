from django.contrib import admin
from .models import Post, Comment
from .forms import PostForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published', 'content_size', 'detail']
    list_display_links = ['id', 'title']
    search_fields = ['title']  # where ilike SQL 로서 수행
    actions = ['make_published']
    # fields = ['title']  # 기존 model form 에 대한 Meta 속성 지정
    form = PostForm  # custom form class

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('comment_set')

    def make_published(self, request, queryset):
        total = queryset.update(published=True)
        self.message_user(request, '{}개의 글을 공개전환했습니다.'.format(total))
    make_published.short_description = "Mark selected stories as published"

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
