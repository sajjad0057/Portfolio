from .models import Contact
from django.shortcuts import HttpResponse

def return_contacts(request):
    try:
        #contact = Contact.objects.all()[0]
        return {
            'contact' : Contact.objects.first()
        }
    except:
        return HttpResponse("<h2>Your contact info in missing , Please update your database contacts table !</h2>")
