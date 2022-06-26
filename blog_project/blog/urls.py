from django.urls import path
from blog import views


app_name = 'blog'
urlpatterns = [
    path('posts', views.BlogListView.as_view(), name='post-list'),
    path('post/add/', views.BlogCreateView.as_view(), name='post-add'),
    path('post/<int:pk>/detail', views.BlogDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.BlogUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.BlogDeleteView.as_view(), name='post-delete'),
]