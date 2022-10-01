from django.shortcuts import render
from .models import receitas

def index(request):
    receitas_dados = receitas.objects.all()

    dados = {
        'lista_receitas' : receitas_dados
    }
    return render(request,'index.html', dados)

def sucodelaranja(request):
    return render(request,'sucodelaranja.html')

def sucodelimao(request):
    return render(request,'sucodelimao.html')

def sucodemanga(resquest):
    return render(resquest,'sucodemanga.html')

def sucodeabacaxi(resquest):
    return render(resquest,'sucodeabacaxi.html')
    
def contato(resquest):
    return render(resquest,'contato.html')