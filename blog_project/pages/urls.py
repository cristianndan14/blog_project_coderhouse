from django.urls import path, include
from pages import views


app_name='page'
urlpatterns = [
    path('about/', views.about, name='about-page'),
    path('', views.PostView.as_view(), name="post-list"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post_add/', views.AddPostView.as_view(), name="post-add"),
    path('post/<int:pk>/edit', views.UpdatePostView.as_view(), name="post-update"),
    path('post/<int:pk>/delete_confirm', views.DeletePostView.as_view(), name="post-delete"),
]