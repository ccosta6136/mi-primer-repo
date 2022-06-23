from django.shortcuts import render
from django.http import HttpResponse
from datetime import  datetime


# Create your views her




def saludo(request):
	return HttpResponse('Hola Django - Coder')

def saludar_a (request, nombre):
    return HttpResponse(f"hola como estas {nombre.upper()}")

