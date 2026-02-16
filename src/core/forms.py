from django import forms

# Formulario para Usuario
class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=250)
    apellido = forms.CharField(max_length=250)

# Formulario para Post
class PostForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    contenido = forms.CharField(widget=forms.Textarea) #  Textarea para que el cuadro sea grande

# Formulario para Categoria
class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=100)