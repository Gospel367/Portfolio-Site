from django.contrib import admin
from .models import AuthorProfile, Project, Category


class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'phone', 'country']
    
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'author',  'created_on']
    search_fields =['title', 'author', 'description']
    prepopulated_fields = {'slug': ('title',)}
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(AuthorProfile, AuthorProfileAdmin)   
admin.site.register(Category, CategoryAdmin)   
