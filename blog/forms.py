from .models import Comment, Contact, Post
from django_summernote.widgets import SummernoteWidget
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('slug', 'updated_on', 'shared_on', 'likes',)
        widgets = {
            'content': SummernoteWidget(),
        }