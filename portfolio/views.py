from django.shortcuts import HttpResponse, render
from .models import About,Services,Portfolio,Testimonial,Contact,Client_message
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    try:
        #about = About.objects.all()[0]
        about = About.objects.first()
        services = Services.objects.all()
        portfolio = Portfolio.objects.all()
        testimonial = Testimonial.objects.all()
        #contact = Contact.objects.all()[0]
        contact = Contact.objects.first()
    except:
        return HttpResponse('<h2>Some thing wrong ! it might be trabule in your database table</h2>')

    # print(f'about ---> {about}\n')
    # print(f'service ---> {service}\n')
    # print(f'portfolio ---> {portfolio}\n')
    # print(f'testimonial ---> {testimonial}\n')
    # print(f'contact ---> {contact}\n')

    return render(request,'index.html',{'about':about,'services':services,'portfolio':portfolio,'testimonial':testimonial,'contact':contact})

    

