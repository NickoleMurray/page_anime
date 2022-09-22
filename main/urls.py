#Contiene las rutas que estan registradas en views
from re import template
from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

#Nombre de la app
app_name = "main"

#Rutas
urlpatterns = [

    path('', views.IndexView.as_view(), name="index"),
    path('blog', views.BlogsView.as_view(), name="blog"),
    path('blogaddinfo/', views.BlogAddInfo, name="blogaddinfo"),
    path('register', views.registerPage, name="register"),
    path('accounts/perfil', views.PerfilView.as_view(), name="profile"),
    
    #Django auth
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name="logout")

] 