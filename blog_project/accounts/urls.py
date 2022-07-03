from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name='account'
urlpatterns = [
    path('login', views.login_request, name='account-login'),
    path('logout', views.logout_request, name='account-logout'),
    path('register', views.register, name='account-register'),
    path('register/update', views.account_update, name='account-update'),
    path('password-change/', views.PasswordsChangeView.as_view(template_name='accounts/change_password.html'), name='change-password'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
    path('profile/', views.profile, name='profile-detail'),
]