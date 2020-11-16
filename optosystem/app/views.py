from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):
    
    return HttpResponse("inicio")

def secretaria(request):

    return HttpResponse("secretaria")

def profesional_Medico(request):

    return HttpResponse("profesional_Medico")

def ventas(request):

    return HttpResponse("ventas")

def taller(request):

    return HttpResponse("taller")

def gerencia(request):

    return HttpResponse("gerencia")

def final(request):
    return HttpResponse("final")


