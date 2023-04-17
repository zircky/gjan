from django.contrib.auth import views as auth_views
from django.urls import path

from demo import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('validate_username', validate_username, name='validate_username'),
    path('validate_name', validate_name, name='validate_name'),
    path('validate_email', validate_email, name='validate_email'),
    path('validate_surname', validate_surname, name='validate_surname'),
    path('validate_patronymic', validate_patronymic, name='validate_patronymic'),

]
