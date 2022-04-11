from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'pagina/inicio.html')

def libros(request):
    return render(request, "libros/index.html")
def nosotros(request):
    return render(request,'pagina/nosotros.html')  
def crear(request):
    return render(request,'libros/crear.html')
def editar(request):
    return render(request,'libros/editar.html')      
              
    
