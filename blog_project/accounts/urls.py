from django.urls import path
from accounts import views


app_name='account'
urlpatterns = [
    path('login', views.login_request, name='account-login'),
    path('logout', views.logout_request, name='account-logout'),
    path('register', views.register, name='account-register'),
    path('register/update', views.account_update, name='account-update'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
]