from django.shortcuts import render

def index(request):
    receitas = {
        1:'Suco de Melão',
        2:'Pizza',
        3:'Suco de Limão',
        4:"Pastel"
    }

    dados = {
        'lista_receitas' : receitas
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