from django.urls import path
from . import views


app_name = 'portfolio'


urlpatterns = [
    path('',views.index,name = 'index'),
    path('portfolio/',views.PortfolioList.as_view(),name='portfolio-list'),
    path('portfolio/<int:pk>/',views.PortfolioDetails.as_view(),name='portfolio-detail'),

]