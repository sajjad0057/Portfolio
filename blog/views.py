from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Blog,Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# class BlogList(ListView):
#     model = Blog
#     paginate_by = 3
#     context_object_name = 'blog'
#     template_name = 'blog.html'



def Bloglist(request):
    blogs = Blog.objects.all()
    page = request.GET.get('page')

    paginator = Paginator(blogs,4)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', { 'blog': blog })
