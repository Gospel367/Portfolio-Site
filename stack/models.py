from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name   
    
    
class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.ManyToManyField(Category)
    tag = models.TextField(max_length=1000, null=True)
    post_content = HTMLField(null=True)

    def __str__(self):
        return self.title
    
