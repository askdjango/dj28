import re
from django import forms


def lnglat_validator(lnglat):
    if not re.match(r'[+-]?\d+\.?\d*,[+-]?\d+\.?\d*', lnglat):
        raise forms.ValidationError('경도,위도를 입력해주세요.')
