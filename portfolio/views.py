from django.shortcuts import HttpResponse, redirect, render
from .models import About,Services,Portfolio,Testimonial,Contact,Portfolio_category
from blog.models import Blog
from .forms import ClientMessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
    try:
        #about = About.objects.all()[0]
        about = About.objects.first()
        services = Services.objects.all()
        portfolio_cat = Portfolio_category.objects.all()
        portfolio = Portfolio.objects.all()
        testimonial = Testimonial.objects.all()
        #contact = Contact.objects.all()[0]
        contact = Contact.objects.first()
        forms = ClientMessageForm()
        blogs = Blog.objects.all()[:3]
    except:
        return HttpResponse('<h2>Some thing wrong ! it might be trabule in your database table</h2>')
    
    if request.method == 'POST':
        form = ClientMessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # form.save()
            messages.warning(request,f'{ name } your message send successfully')
            return render(request,'status.html')
        else:
            messages.warning(request,"your message don't send ! Something wrong")
            return render(request,'status.html')



    return render(request,'index.html',{'about':about,'services':services,'portfolio_cat':portfolio_cat,
            'portfolio':portfolio,'testimonial':testimonial,'contact':contact,'forms':forms,'blogs':blogs})

    

