from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    details = models.TextField()
    image = models.ImageField(upload_to = 'blogs_image',blank=True,null = True)
    slug = models.SlugField(max_length=256,unique=True,allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blogs'

    #generate unique slug
    def _unique_slug_maker(self):
        unique_slug = slugify(self.slug,allow_unicode=True)
        n = 102 # any random rumber
        while Blog.objects.filter(slug = unique_slug).exists():
            unique_slug =  '{}-{}'.format(unique_slug,n)
            n += 30
            return unique_slug

    #save unique slug 
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = self._unique_slug_maker()
        super().save(*args,**kwargs)



class Comment(models.Model):

    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Comments'


