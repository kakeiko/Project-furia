from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.LoginPage, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', views.logoutPage, name="logout"),
    path('atualizar/', views.atualizarTweets, name='atualizar'),
]

