from django.urls import path
from message.views import AddCommentView, UpdateCommentView, DeleteCommentView


app_name='message'
urlpatterns = [
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add-comment'),
    path('post/<int:pk>/comment/edit', UpdateCommentView.as_view(), name='update-comment'),
    path('post/<int:pk>/comment/delete', DeleteCommentView.as_view(), name='delete-comment'),
]