from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    path('',views.BlogList.as_view(),name="blog-list"),
    path('<str:slug>/',views.BlogDetails,name="blog-detail"),
]