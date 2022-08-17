from urllib import request
from django.shortcuts import render
from stack.forms import CreatePostForm
from . models import Post
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy


class PostList(ListView):
    model =Post
    template_name ='home1.html'
    context_object_name ='allposts'


class CreatePost(CreateView):
    model =Post
    form_class = CreatePostForm
    template_name = 'creator.html'
    redirect_authenticated_user = True




    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(CreatePost, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home1.html')
