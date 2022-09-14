from django.shortcuts import render

def Prueba(request):
    return render(request, "index.html",{})
def Blog(request):
    return render(request, "blog.html",{})
def Comentario(request):
    return render(request, "Cbox.html",{})