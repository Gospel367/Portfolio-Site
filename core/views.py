from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import AuthorProfile, Project, Category
from django.views.generic import View,  ListView, DeleteView, DetailView, UpdateView, CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator



class Register(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'  
    
     
     
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    
    def form_valid(self, form):
        user = form.save()
        if user is not  None:
            login(self.request, user)
        return super(Register, self).form_valid(form)
    

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
class CustomLogout(LogoutView):
   pass
    

class Index(View):
    def get(self, request):
        if   request.user.is_authenticated:
            return redirect ('home')
        return render(request, 'index.html')
    
    

class Projhome( ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'homelists'
    
    '''def get_queryset(self):
       self.author = get_object_or_404(Project, name=self.kwargs['author'])
       return Project.objects.filter(author = self.author)'''
   
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['users'] = User.objects.all()
        context['authorcountry'] = AuthorProfile.objects.all()  

        return context
    
class Projdetail(LoginRequiredMixin, DetailView):
    model = Project
    template_name ='projdetail.html'
    context_object_name = 'projdetail'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['authorcountry'] = AuthorProfile.objects.all()
        context['users'] = User.objects.all()
        context['related'] = Project.objects.all().exclude(slug=self.object.slug)
        context['try'] = Category.objects.get(pk =1).project_set.all
        context['author'] = User.objects.get(pk =1).projects.all



        return context

class Createproj(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'create.html'
    success_message = 'Your Project Was Successfully Created'

    fields = ['title', 'category', 'project_image', 'description', 'galleryimage', 'galleryimage2', 'galleryimage3', 'galleryimage4', 'galleryimage5', 'galleryimage6']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(Createproj, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['authorcountry'] = AuthorProfile.objects.all()
        context['users'] = User.objects.all()

        return context
    
    def get_success_url(self):
        return reverse_lazy('create')
    

class Updateproj(SuccessMessageMixin,  LoginRequiredMixin,  UpdateView):
    model = Project
    template_name = 'create.html'
    fields =  ['title', 'slug', 'category', 'project_image', 'description', 'galleryimage', 'galleryimage2', 'galleryimage3', 'galleryimage4', 'galleryimage5', 'galleryimage6'] 
    success_message = 'Your Project Was Successfully Updated'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(Updateproj, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['authorcountry'] = AuthorProfile.objects.all()
        context['users'] = User.objects.all()
        return context
    
 
    def get_success_url(self):
            return reverse_lazy('home')
   
'''class Deleteproj(LoginRequiredMixin, DeleteView) :
    
    def get(self, request, slun):
        item = Project.objects.get(pk = slun)
    
        if self.request.user == item.author:  
            Project.objects.filter(id =slun).delete()
            return redirect('home')
        else:
            return redirect('home')'''
    
'''class Deleteproj(LoginRequiredMixin, DeleteView):
    queryset =Project.objects.all()
    success_url =reverse_lazy('home')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        can_delete  = self.object.can_delete()
        
        if can_delete:
            return super(Deleteproj, self).delete(request, *args, **kwargs)
        else:
            raise Http404('Fuck off')'''
    
def delete_post(request, proj_id):
    items = Project.objects.get(pk =proj_id)
    if request.user == items.author:
        Project.objects.filter(id =proj_id).delete()
        return redirect('author')
    else:
        return HttpResponse("Sorry, You can't perform this action as you are the author of this Post")
    
        
def categorypage(request, pk):
    categories = Category.objects.all()
    categori= Category.objects.get(slug=pk)
    projects = Project.objects.filter(category=categori)
    authorcountry= AuthorProfile.objects.all()
    users = User.objects.all()

    context = {
        'categori': categori,
               'projects': projects,
               'categories': categories,
               'users': users,
               'authorcountry': authorcountry,
               }
    return render(request, 'category.html', context)



def myprojects(request):
    categories = Category.objects.all()
    users = User.objects.all()
    posts = Project.objects.filter(author = request.user)
    profile =AuthorProfile.objects.all
    authorcountry= AuthorProfile.objects.all()

    context = {
        'posts': posts,
                   'categories': categories,
                   'users': users ,
                   'profile': profile,
                   'authorcountry': authorcountry,
                  
    }
    return render( request, 'authors.html', context)


def authorposts(request, author):
    categories = Category.objects.all()
    users = User.objects.all()
    allpost = Project.objects.filter(author=author)
    authorcountry= AuthorProfile.objects.all()

    return render(request, 'authorpage.html', {'allpost': allpost,
                                               'users': users,
                                               "categories": categories,
                                               "authorcountry": authorcountry

                                               })
     


class Createcate(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'createcate.html'
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Createcate, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['users'] = User.objects.all()

        return context
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    
class Createprofile(LoginRequiredMixin, CreateView):
    model = AuthorProfile
    template_name = 'createprofile.html'
    fields = ['username','firstname', 'lastname','email', 'phone', 'country', 'occupation', 'secretword']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Createprofile, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['users'] = User.objects.all()

        return context
    
    def get(self, *args, **kwargs):
        if self.model.objects.filter(user=self.request.user).exists():
            return redirect('myprofile')
        else:
            return super(Createprofile,self).get(*args, **kwargs)
        
    
    def get_success_url(self):
        return reverse_lazy('author')
    
class Myprofile(LoginRequiredMixin, ListView):
    model =AuthorProfile
    template_name = 'myprofile.html'  
    context_object_name ='myprofile' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myprofile'] = context['myprofile'].filter(user=self.request.user)
        context['categories'] = Category.objects.all()
        context['authorcountry'] = AuthorProfile.objects.all()
        context['users'] = User.objects.all()
        
        return context
    
class Updateprofile(LoginRequiredMixin,  UpdateView):
    model = AuthorProfile
    template_name = 'createprofile.html'
    fields =   ['username','firstname', 'lastname','email', 'phone', 'country', 'occupation', 'secretword']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Updateprofile, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['users'] = User.objects.all()
        return context
    
 
    def get_success_url(self):
            return reverse_lazy('myprofile')    
        
      
      
class Allprofiles(LoginRequiredMixin, ListView):
    model =AuthorProfile
    template_name = 'allprofiles.html'  
    context_object_name ='allprofiles' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['users'] = User.objects.all()
        
        return context      
    
    
'''def country(request, country):
    authorcountry = AuthorProfile.objects.all()
    return(request, 'countryposts.html', {'authorcountry': authorcountry})
        '''