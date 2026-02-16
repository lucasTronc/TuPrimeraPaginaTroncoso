from django.shortcuts import render, redirect 
from .models import Usuario, Post, Categoria
from .forms import UsuarioForm
from .models import Post, Categoria 
from .forms import PostForm, CategoriaForm 

def inicio(request):
    return render(request, "core/index.html")

def usuario(request):
    # Vista para VER la lista
    usuarios = Usuario.objects.all()
    return render(request, "core/usuario.html", {"usuario": usuarios})

def crear_usuario(request):
    # Vista para INSERTAR datos
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Guardamos en la DB
            Usuario.objects.create(
                nombre=form.cleaned_data["nombre"],
                apellido=form.cleaned_data["apellido"]
            )
            return redirect("usuarios") # Nos manda a la lista después de guardar
    else:
        form = UsuarioForm()
    return render(request, "core/crear_usuario.html", {"form": form})

def buscar_post(request):
    # Vista de BÚSQUEDA
    titulo = request.GET.get("titulo")
    if titulo:
        resultados = Post.objects.filter(titulo__icontains=titulo)
        return render(request, "core/resultados.html", {"posts": resultados})
    return render(request, "core/buscar.html")

# Formulario para insertar (Post)
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                titulo=form.cleaned_data["titulo"],
                contenido=form.cleaned_data["contenido"]
            )
            return redirect("index")
    else:
        form = PostForm()
    return render(request, "core/crear_post.html", {"form": form})

# Formulario para insertar (Categoria)
def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            Categoria.objects.create(nombre=form.cleaned_data["nombre"])
            return redirect("index")
    else:
        form = CategoriaForm()
    return render(request, "core/crear_categoria.html", {"form": form})