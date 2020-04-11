from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('Hello {} de {} anos' .format(nome, idade))

def soma(request, valor1, valor2):
    return HttpResponse('A soma do valor {} com o valor {} é {}'.format(valor1, valor2, int(valor1)+int(valor2)))