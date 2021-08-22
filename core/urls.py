from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
#handle media file
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',include('portfolio.urls')),
    path('blog/',include('blog.urls')),
    path('', RedirectView.as_view(url='welcome/', permanent=True)),  # initialy  redirect application with 'catalog/' url 
    path('summernote/', include('django_summernote.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


