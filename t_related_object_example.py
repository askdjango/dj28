import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj28.settings")
import django
django.setup()

from blog.models import Post, Comment

'''
# qs = Post.objects.all()
qs = Post.objects.prefetch_related('comment_set').all()

for idx, post in enumerate(qs, 1):
    print(idx, post, post.comment_set.all())
'''

# qs = Comment.objects.all()
qs = Comment.objects.select_related('post').all()

for comment in qs:
    print(comment, comment.post)


from django.db import connection

for q in connection.queries:
    print(q)

print(len(connection.queries), 'queries')
