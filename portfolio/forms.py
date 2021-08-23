from django import forms
from .models import Client_message



# form


class ClientMessageForm(forms.ModelForm):
    class Meta:
        model = Client_message

        fields = ('name','email','subject','message')

        labels ={
            'name' : '',
            'email' : '',
            'subject' : '',
            'message' : '',

        }
        # django.forms.widgets 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name' , }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email',}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject',}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message','style':"max-height: 200px;"}),
        }

    