from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name 
    
    
class AuthorProfile(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank = True, default=User)
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname =models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    country = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200,null = True)
    secretword = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username


    
class Project(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    project_image = models.ImageField(upload_to='media/')
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects', related_query_name='allproj')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, )
    galleryimage = models.ImageField(null = True, upload_to='media/')
    galleryimage2 = models.ImageField(null = True, upload_to='media/')
    galleryimage3= models.ImageField(null = True, upload_to='media/')
    galleryimage4= models.ImageField(null = True, upload_to='media/')
    galleryimage5 = models.ImageField(null = True, upload_to='media/')
    galleryimage6 = models.ImageField(null = True, upload_to='media/')

    
    class Meta:
        ordering = ['-created_on']
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)
    

    