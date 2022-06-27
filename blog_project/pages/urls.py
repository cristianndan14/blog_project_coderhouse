from django.urls import path, include
from pages import views


app_name='page'
urlpatterns = [
    path('pages', views.PageListView.as_view(), name='page-list'),
    path('page/add/', views.PageCreateView.as_view(), name='page-add'),
    path('page/<int:pk>/detail', views.PageDetailView.as_view(), name='page-detail'),
    path('page/<int:pk>/update', views.PageUpdateView.as_view(), name='page-update'),
    path('page/<int:pk>/delete', views.PageDeleteView.as_view(), name='page-delete'),
    # path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]