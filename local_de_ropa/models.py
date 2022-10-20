from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Remeras(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    talle = models.CharField(max_length=5)
    color =  models.CharField(max_length=40)
    stock = models.IntegerField()

    def __str__(self) :
        return f"modelo: {self.modelo} -- marca: {self.marca} -- talle: {self.talle} -- color: {self.color} -- stock:{self.stock}"

class Buzos(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    talle = models.CharField(max_length=5)
    color =  models.CharField(max_length=40)
    stock = models.IntegerField()

    def __str__(self) :
        return f"modelo: {self.modelo} -- marca: {self.marca} -- talle: {self.talle} -- color: {self.color} -- stock:{self.stock}"


class Jeans(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    talle = models.CharField(max_length=5)
    color =  models.CharField(max_length=40)
    stock = models.IntegerField()

    def __str__(self) :
        return f"modelo: {self.modelo} -- marca: {self.marca} -- talle: {self.talle} -- color: {self.color} -- stock:{self.stock}"

class Camperas(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    talle = models.CharField(max_length=5)
    color =  models.CharField(max_length=40)
    stock = models.IntegerField()

    def __str__(self) :
        return f"modelo: {self.modelo} -- marca: {self.marca} -- talle: {self.talle} -- color: {self.color} -- stock:{self.stock}"    


class Avatar (models.Model):
    #viculo con el usuario
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    #carpeta de imagenes
    image =models.ImageField(upload_to ="avatares",null = True,blank = True)