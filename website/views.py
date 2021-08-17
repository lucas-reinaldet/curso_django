from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Contact
def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'HTML', 'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi']

    lista_post =  Post.objects.filter(approved=True)

    data = {'name': 'Curso de Django 3', 
    'lista_tecnologias': lista,
    'posts': lista_post    
    }

    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})


def save_form(request):

    Contact.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        message = request.POST['message']
    )

    return render(request, 'contact_success.html')
