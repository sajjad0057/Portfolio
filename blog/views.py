from django.contrib import messages
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView,DetailView,CreateView
from .models import Blog,Comment
from .forms import CommentForm

# Create your views here.

class BlogList(ListView):
    model = Blog
    paginate_by = 6
    context_object_name = 'blog'
    template_name = 'blog.html'


# class BlogDetails(DetailView):
#     model = Blog
#     context_object_name = "blog"
#     template_name = 'blog_details.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['forms'] = CommentForm()
#         return context

def BlogDetails(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    #print('blog ---->',blog)
    forms = CommentForm()
    if request.method == 'POST':
        forms = CommentForm(request.POST)
        if forms.is_valid():
            # print('blog ---->',blog.id)
            name = forms.cleaned_data['name']
            form=forms.save(commit=False)
            form.blog = blog    
            form.save()
            messages.warning(request,f'{name} Thanks for your comment ')
            return HttpResponseRedirect(reverse('blog:blog-detail',kwargs={'slug':slug}))
        else:
            messages.danger("Something Wrong ! your Comment doesn't submitted !")
            return HttpResponseRedirect(reverse('blog:blog-detail',kwargs={'slug':slug}))

    return render(request,'blog_details.html',{'blog':blog,'forms':forms})





