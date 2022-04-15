from django.shortcuts import render,redirect

from sistema.models import Libro
from .forms import LibroForm

# Create your views here.
def inicio(request):
    return render(request, "pagina/inicio.html")


def libros(request):
    libros = Libro.objects.all()
    return render(request, "libros/index.html", {"libros": libros})


def nosotros(request):
    return render(request, "pagina/nosotros.html")


def crear(request):
    formulario = LibroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, "libros/crear.html", {'formulario': formulario})


def editar(request,id):
    libro=Libro.objects.get(id=id)
    formulario=LibroForm(request.POST or None, request.FILES or None , instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, "libros/editar.html",{'formulario':formulario})

def eliminar(request,id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')
    return render(request,"libros/eliminar.html")    
# 2:16 llegue