from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'HTML', 'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi']

    lista_post =  Post.objects.filter(approved=True)

    data = {'name': 'Curso de Django 3', 
    'lista_tecnologias': lista,
    'posts': lista_post    
    }

    return render(request, 'index.html', data)