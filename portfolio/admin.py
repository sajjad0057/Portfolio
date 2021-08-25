from django.contrib import admin
from .models import About,Services,Portfolio,Testimonial,Contact,Client_message,Portfolio_category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('about_details',)
    # list_display = ('home_bg_image','about_img','happy_client','year_of_experience','number_of_projects','number_of_awards')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ( 'service_name','service_text' )







class PortfolioAdmin(SummernoteModelAdmin):
    summernote_fields = ('project_details',)
    list_display = ('category','project_image','project_name','project_url','project_date')



class TestimonialAdmin(SummernoteModelAdmin):
    summernote_fields = ('client_comment',)
    list_display = ('client_name','client_title','client_image')



class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'facebook_url','twitter_url','instagram_url','linkdin_url','Email','phone' )


class ClientMessageAdmin(admin.ModelAdmin):
    list_display = ('name','send_time')


admin.site.register(About,AboutAdmin)
admin.site.register(Services,ServiceAdmin)
admin.site.register(Portfolio_category)
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Client_message,ClientMessageAdmin)
