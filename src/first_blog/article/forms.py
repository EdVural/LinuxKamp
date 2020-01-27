from django import forms
from .models import Post


class ArticleForm(forms.Form):
    header = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    liked = forms.IntegerField()
    draft = forms.BooleanField()


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ('owner',)
