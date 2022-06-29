from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from pages.models import Post
from .forms import PostForm, EditPostForm

def about(request):
    return render(request, "pages/about.html")


class PostView(ListView):
    model = Post
    template_name= 'post_list.html'
    ordering = ['-post_date']



class PostDetailView(DetailView):
    model= Post
    template_name= 'pages/post_details.html'


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/post_add.html'
    #fields = '__all__'

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'pages/post_update.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('page:post-list')
    template_name = 'pages/post_delete.html'