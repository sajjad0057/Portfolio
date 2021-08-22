from django.contrib import admin
from .models import About,services,portfolio,testimonial,contact,client_message

# Register your models here.



admin.site.register(About)
admin.site.register(services)
admin.site.register(portfolio)
admin.site.register(testimonial)
admin.site.register(contact)
admin.site.register(client_message)
