from urllib.parse import urlencode
from django.conf import settings
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

    @property
    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[-1]
        return None

    @property
    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]
        return None

    def get_lnglat_naver_static_url(self, width=72, height=72, level=8):
        if self.lnglat:
            url = 'https://openapi.naver.com/v1/map/staticmap.bin'
            params = {
                'url': 'http://localhost:8000',
                'clientId': settings.NAVER_APP_CLIENT_ID,
                'center': self.lnglat,
                'level': level,
                'w': width,
                'h': height,
                'baselayer': 'default',
                'markers': self.lnglat,
            }
            return url + '?' + urlencode(params)
        return None


class Comment(models.Model):
    post = models.ForeignKey(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
