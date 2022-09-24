from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sucodelaranja', views.sucodelaranja, name='sucodelaranja'),
    path('sucodelimao', views.sucodelimao, name='sucodelimao'),
    path('sucodemanga', views.sucodemanga, name='sucodemanga'),
    path('sucodeabacaxi', views.sucodeabacaxi, name='sucodeabacaxi'),
    path('contato', views.contato, name='contato'),
    ]


