from django.urls import path, include
from pages import views


app_name='page'
urlpatterns = [
    path('', views.PageListView.as_view(), name='page-list'),
    path('add/', views.PageCreateView.as_view(), name='page-add'),
    path('<int:pk>/detail', views.PageDetailView.as_view(), name='page-detail'),
    path('<int:pk>/update', views.PageUpdateView.as_view(), name='page-update'),
    path('<int:pk>/delete', views.PageDeleteView.as_view(), name='page-delete'),
    path('about/', views.about, name='about-page'),
    # path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]