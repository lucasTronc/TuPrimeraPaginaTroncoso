from django.shortcuts import render, redirect 
from .models import Usuario, Post, Categoria
from .forms import UsuarioForm
from .models import Post, Categoria 
from .forms import PostForm, CategoriaForm 
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm

def inicio(request):
    posts = Post.objects.all() 
    return render(request, "core/index.html", {"posts": posts})

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
            return redirect("usuarios") # manda a la lista después de guardar
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

def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # 'instance' carga los datos actuales
        if form.is_valid():
            form.save() # Al usar ModelForm, esto es más simple
            return redirect("index")
    else:
        form = PostForm(instance=post)
    return render(request, "core/crear_post.html", {"form": form, "editando": True})

# --- ELIMINAR POST ---
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("index")
    return render(request, "core/eliminar_confirmar.html", {"post": post})

#--- función de registro ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

#--- devuelve un HTML con mi info ---
def about(request):
    return render(request, "core/about.html")