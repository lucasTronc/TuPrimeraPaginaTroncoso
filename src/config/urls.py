from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.inicio, name='index'),
    path('admin/', admin.site.urls),
    path("usuarios/", views.usuario, name="usuarios"),
    path("usuarios/nuevo/", views.crear_usuario, name="crear_usuario"),
    
    path("post/nuevo/", views.crear_post, name="crear_post"),
    path("categoria/nuevo/", views.crear_categoria, name="crear_categoria"),
    path("buscar/", views.buscar_post, name="buscar_post"),

    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    path('post/editar/<int:pk>/', views.editar_post, name='editar_post'),
    path('post/eliminar/<int:pk>/', views.eliminar_post, name='eliminar_post'),
    path('about/', views.about, name='about'),
]