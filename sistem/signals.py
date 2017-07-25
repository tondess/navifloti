from django.db import models
from sistem.models import *
from datetime import datetime
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save, post_delete, pre_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out

G_usr = 'ANONIMO'
#variable global para guardar el nombre de usuario

@receiver([user_logged_in, user_logged_out])
def registro_e(sender, user, request, **kwargs):
    signal = kwargs.get('signal', None)
    session_key = request.session.session_key
    global G_usr
    G_usr = '%s' %user.username

    if signal == user_logged_in:
        accion = "Entrada al sistema"
    elif signal == user_logged_out:
        accion = "salida del sistema"

    registro = UserLog(usuario=G_usr, accion=accion, modulo=request.path, sesion=session_key, fecha_hora=datetime.now())
    registro.save()


@receiver(post_save, sender=prueba)
def registrar_pru(sender, instance, using, **kwargs):
    post_save.disconnect(registrar_pru)
    signal = kwargs.get('signal', None) 

    if signal == post_save:
        accion = 'Se Creó: %s' %instance

    registro = UserLog(usuario=G_usr, accion='Se creo una prueba', modulo='Pruebas/crear_pruebas', sesion='no posee', fecha_hora=datetime.now())
    registro.save()
    post_save.connect(registrar_pru)

@receiver(post_delete, sender=preguntas)
def registrar_pre(sender, instance, using, **kwargs):
    registro = UserLog(usuario=G_usr, accion='Se elimino un objeto del modulo preguntas', modulo='Prueba/Preguntas', sesion='no posee', fecha_hora=datetime.now())
    registro.save()

