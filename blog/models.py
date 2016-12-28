from django.db import models
from .validators import lnglat_validator


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    lnglat = models.CharField(max_length=100, validators=[lnglat_validator],
        blank=True)
    published = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
