from django.contrib import admin
from . models import Category, Post, Tags

admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Category)
