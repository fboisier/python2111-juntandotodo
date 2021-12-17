from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
RUT_CHILENO_REGEX = re.compile(r'^[0-9]+[-|‐]{1}[0-9kK]{1}$')
MAYUSCULA_PUNTO_REGEX = re.compile(r'^[A-Z].*[.]$')

# Mínimo ocho caracteres, al menos una letra mayúscula, una letra minúscula y un número:
PASSWORD_SEGURA_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')


class CamionManager(models.Manager):
    def saludar(self, nombre):
        return "HOLA "+nombre
    
    def validar(self, postData):
        print("DESDE VALIDAR: ",postData)
        
        error = {}
        
        if len(postData['nombre']) < 10:
            error['nombre'] = "El nombre debe tener más de 10 caracteres."
            
        if int(postData['tonelaje']) <= 0:
            error['tonelaje'] = "El tonelaje debe ser mayor a 0"
            
        if not MAYUSCULA_PUNTO_REGEX.match(postData['marca']):
            error['marca'] = "La marca debe empezar con mayuscula y terminar con un punto."
        
        return error

# Create your models here.
class Camion(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    tonelaje = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # rutas = todas las rutas del camion.
    
    objects = CamionManager()
    
    def __str__(self):
        return f"Camion: {self.nombre} {self.marca} {self.tonelaje}"
    def __repr__(self):
        return f"Camion: {self.nombre} {self.marca} {self.tonelaje}"
    
class Ruta(models.Model):
    camion = models.ForeignKey(Camion, related_name="rutas", on_delete=models.CASCADE)
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    kilometros = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"RUTA: {self.camion.nombre} {self.origen} {self.destino} {self.kilometros}"
    def __repr__(self):
        return f"RUTA: {self.camion.nombre} {self.origen} {self.destino} {self.kilometros}"