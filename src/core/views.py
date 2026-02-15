from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    return HttpResponse("hola Django")

def saludar_con_etiqueta(request):
    return HttpResponse('<h1>"hola Django"</h1>')

def index(request):
    return render(request, 'core/index.html',{"titulo":"Django"})
    
def notas(request):
    mis_notas = [10,7,4,6]
    return render(request, "core/notas.html", context={"notas" : mis_notas})

