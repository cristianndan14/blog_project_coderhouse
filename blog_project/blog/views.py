from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "post/post_list.html"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "post/post_detail.html"
    fields = ['title', 'date']


class BlogCreateView(CreateView):
    model = Blog
    success_url = reverse_lazy('blog:post-list')
    fields = ['title', 'subtitle', 'body']


class BlogUpdateView(UpdateView):
    model = Blog
    success_url = reverse_lazy('blog:post-list')
    fields = ['title', 'subtitle', 'body']


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:post-list')