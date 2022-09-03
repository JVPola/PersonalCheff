# PersonalCheff
<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
<img src="exemplo.webp" alt="exemplo imagem">
> Uma aplicação web de receita chamada PersonalCheff desenvolvida durante o curso de Python no Senac Americana. A aplicação listará receitas e clicando em cada nome de receita você pode ver a receita completa.
### Lista de tarefas
Segue a lista de tarefas a serem desenvolvidas no projeto:
- [X] Pré-requisitos
    - [X] Instalar o Python
    - [X] Instalar Visual Studio Code
- [X] Criar e ativar o ambiente virtual
```
Criar: python -m venv .\venv\
Ativar: venv\Scripts\activate
```
- [X] Instalar o Django
```
python -m pip install django==3.2
```
- [X] Criar o projeto PersonalCheff
```
django-admin.py startproject PersonalCheffProj
```
- [X] Subir o servidor e testar o projeto
```
entrar na pasta do projeto (para entrar na pasta): cd personalCheffProj
python manage.py runserver
```
- [X] Alterar o idioma para `pt-br`
```
pasta "settings.py" trocar idioma na linha 106 
```
- [X] Alterar o timezone do projeto para `America/São_paulo`
```
pasta "settings.py" trocar trocar timezone linha 108 America/Sao_Paulo
```
- [X] Criar o APP receitas
```
* Preciso estar dentro da pasta d projeto (PersonalCheffProj)
python manage.py startapp receitas
```
- [X] Registrar o APP receitas
```
pasta "settings.py" na linha 33 (INSTALLED_APPS) adicionar 'receitas'
```
- [X] Configurar a rota inicial (index)
```
na pasta "receitas" criar o arquivo urls.py

from platform import python_branch

from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index')
]
```
- [x] Criar a view para a rota inicial 
```
Dentro da pasta receitas(app) abrir o arquivo 'view'

from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Seja bem vindo</h1>")
```
- [ ] criar o arquivo index
```
-Dentro da pasta receitas(app), crie a pasta `templates`
-Dentro da pasta templates, crie seus arquivos HTML, começando pelo index.html
-No arquivo views.py que esta dentro da pasta do app(receitas) faça a seguinte alteração no codigo:

from django.shortcuts import render

def index(request):
    return render(request,'index.html')

```
## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
[⬆ Voltar ao topo](#nome-do-projeto)<br>