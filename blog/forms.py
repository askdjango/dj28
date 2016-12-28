from django import forms
from .models import Post
from .widgets import NaverMapPointWidget


class PostForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data.get('title', None)
        if title:
            if len(title) % 2 == 0:
                raise forms.ValidationError('홀수로 입력하시오.')
        return title

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'lnglat': NaverMapPointWidget(attrs={'width': '100%', 'height': '400px'}),
        }
        # fields = ['title', 'content']
