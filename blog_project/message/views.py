from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comment
from .forms import CommentForm, EditCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'message/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class UpdateCommentView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = EditCommentForm
    template_name = 'message/update_comment.html'


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'message/delete_comment.html'
    success_url = reverse_lazy('page:post-list')