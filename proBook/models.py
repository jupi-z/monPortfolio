from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default='/article')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    publish = models.BooleanField()

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    sujet = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} {self.sujet} {self.email}'


class Project(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title
