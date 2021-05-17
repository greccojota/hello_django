from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))

def calc(request, n1, n2, op):
    result = 0
    if 'soma' in op:
        result = n1+n2
    elif 'sub' in op:
        result = n1-n2
    elif 'div' in op:
        result = n1/n2
    elif 'multi' in op:
        result = n1*n2

    return HttpResponse('<h2>Resultado da {}: {}<h2>'.format(op, result))