from django.urls import path
from blog import views


app_name = 'blog'
urlpatterns = [
    path('blogs', views.BlogListView.as_view(), name='blog-list'),
    path('blog/add/', views.BlogCreateView.as_view(), name='blog-add'),
    path('blog/<int:pk>/detail', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog-delete'),
]