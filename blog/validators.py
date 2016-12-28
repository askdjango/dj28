import re
from django import forms

LNGLAT_REGEX = r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$'

def lnglat_validator(lnglat):
    if not re.match(LNGLAT_REGEX, lnglat):
        raise forms.ValidationError('경도,위도를 입력해주세요.')
