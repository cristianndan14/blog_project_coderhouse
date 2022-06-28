from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from pages.models import Page
from message.models import Comment


class PageListView(ListView):
    model = Page
    template_name = "pages/page_list.html"


class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page_detail.html"
    fields = ['title', 'subtitle', 'date', 'image', 'account', 'content_post']


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    success_url = reverse_lazy('page:page-list')
    fields = ['title', 'subtitle', 'image', 'content_post']


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    success_url = reverse_lazy('page:page-list')
    fields = ['title', 'subtitle', 'image', 'content_post']


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('page:page-list')