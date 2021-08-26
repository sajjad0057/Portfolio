from django.db.models.base import Model
from django.shortcuts import HttpResponse, redirect, render
from .models import About,Services,Portfolio,Testimonial,Portfolio_category
from blog.models import Blog
from .forms import ClientMessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DetailView,ListView


# Create your views here.

@login_required
def index(request):
    try:
        #about = About.objects.all()[0]
        about = About.objects.first()
        services = Services.objects.all()
        portfolio_cat = Portfolio_category.objects.all()
        portfolio = Portfolio.objects.all()[:6]
        testimonial = Testimonial.objects.all()
        forms = ClientMessageForm()
        blogs = Blog.objects.all()[:3]
    except:
        return HttpResponse('<h2>Something wrong ! it might be problem in your database table, please insert all table data</h2>')
    
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
            'portfolio':portfolio,'testimonial':testimonial,'forms':forms,'blogs':blogs})





class PortfolioList(ListView):
    model = Portfolio
    paginate_by = 8
    context_object_name = 'portfolio'
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio_cat'] = Portfolio_category.objects.all()
        return context


    

class PortfolioDetails(DetailView):
    model = Portfolio
    context_object_name = 'portfolio'
    template_name = 'portfolio-details.html'