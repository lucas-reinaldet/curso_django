from django.db import models

class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField() #tamanho em aberto
    categories = models.CharField(max_length=2,
                        choices=Categorias.choices,
                        default=Categorias.GR)
    approved = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):

        return self.title

    def full_name(self):
        return self.title + ' ' + self.sub_title

    full_name.admin_order_field = 'title'

class Contact(models.Model):

    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()