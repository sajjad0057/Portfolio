from django import forms
from django import forms
from django.forms import fields
from .models import Comment


# create comment 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields = ('name','comment')
    
        labels ={
            'name' : '',
            'comment':'',

        }
        # django.forms.widgets 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name' , }),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Your Comment','style':"max-height: 200px;"}),
        }


