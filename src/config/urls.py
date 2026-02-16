from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    
    path('', views.inicio, name='index'),
    path('admin/', admin.site.urls),
    path("usuarios/", views.usuario, name="usuarios"),
    path("usuarios/nuevo/", views.crear_usuario, name="crear_usuario"),
    
    # NUEVAS RUTAS PARA LA CONSIGNA:
    path("post/nuevo/", views.crear_post, name="crear_post"),
    path("categoria/nuevo/", views.crear_categoria, name="crear_categoria"),
    path("buscar/", views.buscar_post, name="buscar_post"),
]