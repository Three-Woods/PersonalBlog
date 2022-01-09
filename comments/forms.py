from django import  forms
from .models import Comment

class CommentForm(forms.ModelForm):
    #Meta: inner class
    class Meta:
        #The forms is belong to Comment class
        model = Comment
        #fields: Specifies the fields that the form needs to display
        fields = ['name','email','url','text']

