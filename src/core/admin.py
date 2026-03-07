from django.contrib import admin
from .models import Usuario, Categoria, Post

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Post)