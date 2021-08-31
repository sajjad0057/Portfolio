from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
#handle media file
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',include('portfolio.urls')),
    path('blogs/',include('blog.urls')),
    path('', RedirectView.as_view(url='welcome/', permanent=True)),  # initialy  redirect application with 'catalog/' url 
    path('summernote/', include('django_summernote.urls')),

    # """
    # Views and functions for serving static files. These are only to be used
    # during development, and SHOULD NOT be used in a ******production****** setting.
    # """
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

] 




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)