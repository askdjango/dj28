import re
from django import forms
from django.template.loader import render_to_string
from django.conf import settings
from .validators import LNGLAT_REGEX


class NaverMapPointWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        parent_html = super().render(name, value, attrs)
        if attrs is None:
            attrs = {}

        lng, lat = '127.0276522', '37.4979882'  # 강남역
        if value:
            matched = re.match(LNGLAT_REGEX, value)
            if matched:
                lng, lat = matched.groups()

        width = str(self.attrs.get('width', '100%'))
        height = str(self.attrs.get('height', '300'))
        if width.isdigit():
            width += 'px'
        if height.isdigit():
            height += 'px'

        context = dict(self.attrs, **attrs)
        context.update({
            'naver_app_client_id': settings.NAVER_APP_CLIENT_ID,
            'width': width,
            'height': height,
            'lng': lng,
            'lat': lat,
        })

        html = render_to_string('blog/naver_map_point_widget.html', context)
        return parent_html + html
