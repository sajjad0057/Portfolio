from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import CharField

# Create your models here.


class About(models.Model):
    home_bg_image = models.ImageField(upload_to = 'about_images',verbose_name="Set home Background Image")
    about_img = models.ImageField(upload_to = 'about_images',verbose_name="Set about section image")
    about_details = models.TextField(verbose_name="Write Details about you")
    happy_client = models.IntegerField(default=0)
    year_of_experience = models.IntegerField(default=0)
    number_of_projects = models.IntegerField(default=0)
    number_of_awards = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'About Section'

    def __str__(self):
        return "abouts"




class Skill(models.Model):
    title = models.CharField(max_length=120)
    skill_value = models.PositiveIntegerField(
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='set your skill value out of 100'
        )

    class Meta:
        verbose_name_plural = 'Skills Section'

    def __str__(self):
        return self.title






class Resume_Category(models.Model):
    category = CharField(max_length=120,help_text='set your resume title - like as Education , Professional Experience')

    class Meta:
        verbose_name_plural = 'Resume Category'
    
    def __str__(self):
        return self.category


class Resume(models.Model):
    category = models.ForeignKey(Resume_Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    duration = models.CharField(max_length=20,help_text='set working durations like as , 2017 - 2020 or now')
    location  = models.CharField(max_length=250,help_text='Set your institue or workspace name and location')
    details = models.TextField(help_text='Set your position Details')


    class Meta:
        verbose_name_plural = 'Resume Section'

    def __str__(self):
        return self.title



class Services(models.Model):
    service_name = models.CharField(max_length=256)
    service_text = models.CharField(max_length=512)

    class Meta:
        verbose_name_plural = 'Service Section'

    def __str__(self):
        return self.service_name






class Portfolio_category(models.Model):
    category = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Portfolio Category'

    def __str__(self):
        return self.category






class Portfolio(models.Model):
    category = models.ForeignKey(Portfolio_category,on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to = "project_image")
    project_name = models.CharField(max_length=128)
    project_details = models.TextField()
    project_url = models.URLField(blank=True,null=True)
    project_date = models.DateField(blank=True,null=True)


    class Meta:
        verbose_name_plural = 'Portfolio Section'
        ordering = ("-id",)

    def __str__(self):
        return self.project_name



class Testimonial(models.Model):
    client_name = models.CharField(max_length=64)
    client_title = models.CharField(max_length=128,blank=True,null=True)
    client_image = models.ImageField(upload_to = "client_images",blank=True,null=True)
    client_comment = models.TextField()

    class Meta:
        verbose_name_plural = 'Testimonial Section'


    def __str__(self):
        return self.client_name




class Contact(models.Model):
    facebook_url = models.URLField(blank=True,null=True)
    twitter_url = models.URLField(blank=True,null=True)
    instagram_url = models.URLField(blank=True,null=True)
    linkdin_url = models.URLField(blank=True,null=True)
    Email = models.EmailField()
    phone = models.CharField(max_length=32,blank=True,null=True)


    class Meta:
        verbose_name_plural = 'Contact Section'



    def __str__(self):
        return self.phone





class Client_message(models.Model):
    name = models.CharField(max_length=64,)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Client Message Section'

    def __str__(self):
        return f'{ self.name } - { self.email }'









    



