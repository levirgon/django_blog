from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
# extending ListView


class BlogListView(ListView):
    model = BlogPost
    template_name = "home.html"
    context_object_name = 'blog_posts'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "post_detail.html"
    context_object_name = 'blog_item'


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "post_new.html"
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'blog_item'
