from django.shortcuts import render

def Inicio(request):
    return render (request, "Barrientos/inicio.html")
def Registro(request):
    return render (request, "Barrientos/formregistro.html")