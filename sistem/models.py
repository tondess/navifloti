from django.db import models
from django.contrib.auth.models import AbstractUser


class UserLog(models.Model):
    usuario = models.CharField(max_length=40)
    accion = models.CharField(max_length=40)
    modulo = models.CharField(max_length=40)
    sesion = models.CharField(max_length=40)
    fecha_hora = models.DateTimeField()

    class Meta:
       ordering = ['-id']

    def __str__(self):
        return self.usuario

class User(AbstractUser):
    ci = models.IntegerField(primary_key=True)
    tipo_usuario = models.CharField(max_length=20)
    esp= models.CharField(max_length=20)

    def __str__(self):
        return self.username

class prueba(models.Model):
    cod_prueba = models.AutoField(primary_key=True)
    ci_p = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    valor = models.IntegerField()
    seccion = models.CharField(max_length=20)
    titulo = models.CharField(max_length=250)
    fecha = models.DateField()
    hora = models.CharField(max_length=20)
    Duracion = models.CharField(max_length=20)
    activa = models.BooleanField(default=True)


class preguntas(models.Model):
    cod_pregunta = models.AutoField(primary_key=True)
    cod_p = models.ForeignKey(prueba, null=True, blank=True, on_delete=models.CASCADE) 
    ponderacion = models.IntegerField()
    pregunta = models.CharField(max_length=200)
    r1 = models.CharField(max_length=200)
    r2 = models.CharField(max_length=200)
    r3 = models.CharField(max_length=200)
    r4 = models.CharField(max_length=200)
    rc = models.CharField(max_length=10)

class solucionex(models.Model):
    cod_solex = models.AutoField(primary_key=True)
    cod_pru = models.ForeignKey(prueba, null=True, blank=True, on_delete=models.CASCADE)
    ci_e = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  

class solucionpr(models.Model):
    cod_respuesta = models.AutoField(primary_key=True)
    cod_examen = models.ForeignKey(solucionex, null=True, blank=True, on_delete=models.CASCADE)
    ponderacion = models.IntegerField()
    pregunta = models.CharField(max_length=200)
    respuesta = models.CharField(max_length=10)
    ci_e = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class nota(models.Model):
    ci_e = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    nota = models.CharField(max_length=10)
    cod_p = models.ForeignKey(prueba, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()