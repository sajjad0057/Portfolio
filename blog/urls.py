from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [

    path('',views.Bloglist,name="blog-list"),
    # path('',views.BlogList.as_view(),name="blog-list"),
]