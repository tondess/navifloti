from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib import messages, auth
from django.contrib.auth import update_session_auth_hash, authenticate
from django.contrib.auth.views import login
from django.contrib.messages.views import SuccessMessageMixin
from django.template import RequestContext
from sistem.models import *
from sistem.forms import *
from datetime import datetime
from django.db.models import Q

# login

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)
		if user is not None: 
			if user.is_active:
				login(request, user)
				# Redirect to index page.
				return HttpResponseRedirect("/inicio/")
			else:
				# Return a 'disabled account' error message
				messages.error(request, 'Usuario inactivo, comuniquese con el Administrador de NAVIFLOTI')
				return redirect('login') 
		else:
			# Return an 'invalid login' error message.
			messages.error(request, 'Nombre de Usuario o Contraseña Erroneos')
			return render_to_response('login/login.html', {}, context)
	else:
		# the login is a  GET request, so just show the user the login form.
		return render_to_response('login/login.html', {}, context)

# INICIO

class inicio(TemplateView):
	template_name = 'base/base.html'

# PERFIL DE USUARIO

def perfil(request):
	if User.is_authenticated:
		username = request.user
		registro = UserLog(usuario=username, accion='entrada a modulo perfil', modulo='Perfil', sesion='no_aplica', fecha_hora=datetime.now())
		registro.save()
	return render(request, 'perfil/perfil.html')


# GESTION DE USUARIOS

def cu(request):
	usr_act=request.user
	if request.method == 'GET':
		form = usrform()
	else:
		form = usrform(request.POST)
		usern=request.POST['username']
		usrb='Se Creo el Usuario {0} '.format(usern) 
		if form.is_valid():
			form.save()
			registro = UserLog(usuario=usr_act.username , accion=usrb, modulo='Usuario', sesion='no_aplica', fecha_hora=datetime.now())
			registro.save()
			messages.success(request, 'Usuario Creado Exitosamente')
			return redirect('vista1')
	return render(request, 'vista_usuario/c_usu.html', {'form':form})

#FUNCION QUE LISTA USUARIOS

class lusu(ListView):
	model = User
	template_name = 'vista_usuario/list_usu.html'
	paginate_by = 8

#FUNCION QUE MODIFICA USUARIOS

def modu(request, ci):
	query=User.objects.get(ci=ci)
	usr_act=request.user
	usrb='Se Modifico el Usuario {0} '.format(query.username) 
	if query.is_active == True:
		if request.method == 'GET':
			form = modusrform(instance=query)
		else:
			form = modusrform(request.POST, instance=query)
			if form.is_valid():
				form.save()
				registro = UserLog(usuario=usr_act , accion=usrb, modulo='Usuario', sesion='no_aplica', fecha_hora=datetime.now())
				registro.save()
				messages.success(request, 'Datos Modificados Satisfactoriamente')	
				return redirect('vista2')
		return render(request, 'vista_usuario/m_usu.html', {'form':form})
	else:
		messages.error(request, 'El Usuario no se Puede Modificar Por Que Esta Inactivo.')
		return redirect('vista2')
			
class eliu(DeleteView):
	model = User
	template_name = 'vista_usuario/eli_usu.html'
	success_url = reverse_lazy('vista2')

#FUNCION QUE ACTIVA Y DESACTIVA USUARIOS

def act_dct_usu(request, ci):
	act=User.objects.get(ci=ci)
	usr_act=request.user
	usrb='Se Desactivo el Usuario {0} '.format(act.username) 
	usrb1='Se Activo el Usuario {0} '.format(act.username) 
	if usr_act.ci == act.ci:
		messages.warning(request, 'Por razones de seguridad no puedes desactivar tu usuario')
		return redirect('vista2')
	else:
		if act.is_active == True:
			act.is_active = False
			act.save()
			registro = UserLog(usuario=usr_act.username , accion=usrb, modulo='Usuario', sesion='no_aplica', fecha_hora=datetime.now())
			registro.save()
			messages.warning(request, 'Usuario Desactivado')
		else:
			act.is_active = True
			act.save()
			registro = UserLog(usuario=usr_act.username , accion=usrb1, modulo='Usuario', sesion='no_aplica', fecha_hora=datetime.now())
			registro.save()
			messages.success(request, 'Usuario Activado')
		return redirect('vista2')

#FUNCION QUE CAMBIA LAS CONTRASEÑAS

def camb_contra(request):
	usr_act=request.user

	if request.method == 'POST':
		form = camb_c(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			registro = UserLog(usuario=usr_act.username , accion='Cambio de Contraseña', modulo='Cambiar Contraseña', sesion='no_aplica', fecha_hora=datetime.now())
			registro.save()
			update_session_auth_hash(request, user) # Important!
			messages.success(request, 'Contraseña Cambiada')
			return redirect('perfil')
	else:
		form = camb_c(request.user)
	return render(request, 'vista_usuario/c_contra.html', {'form': form})


# logica del modulo PRUEBA
#CLASE QUE CREA LAS PRUEBAS 


class cp(SuccessMessageMixin, CreateView):
	model = prueba
	template_name = 'prueba/cre_pru.html'
	form_class = pruebaform
	success_url = reverse_lazy('crearp') 
	success_message='Prueba Creada Exitosamente'

class lpda(ListView):
	queryset = prueba.objects.order_by('-ci_p')
	template_name = 'prueba/list_pru.html'
	paginate_by = 8

def lp(request):
	query = prueba.objects.filter(ci_p=request.user.ci)
	contexto = {'object_list':query}
	return render(request, 'prueba/list_pru.html', contexto)
	paginate_by = 8
	


#CLASE QUE MODIFICA LAS PRUEBAS YA CREADAS

class modp(SuccessMessageMixin, UpdateView):
	model = prueba
	template_name = 'prueba/cre_pru.html'
	form_class = pruebaform
	success_url = reverse_lazy('gesp')
	success_message='Prueba Modificada Exitosamente'

def cap_id(request, cod_prueba):
	query=prueba.objects.get(cod_prueba=cod_prueba)
	context = {'object': query}
	return redirect('c_preg', context)


#FUNCION QUE CREA LAS PREGUNTAS PARA UNA DETERMINADA PRUEBA

def c_pre(request, cod_prueba):
	id_p=prueba.objects.get(cod_prueba=cod_prueba)

	if id_p.activa == True:
		if request.method == 'POST':
			usr_act=request.user 
			usrb='Pregunta creada para la Pueba Codigo: {0} '.format(id_p.cod_prueba)
			registro = preguntas(cod_p = id_p, ponderacion = request.POST['ponderacion'], pregunta = request.POST['pregunta'], r1 = request.POST['r1'], r2 = request.POST['r2'], r3 = request.POST['r3'], r4 = request.POST['r4'],rc = request.POST['rc'])
			registro1 = UserLog(usuario=usr_act.username , accion=usrb, modulo='pruebas/crear_pregunta', sesion='no_aplica', fecha_hora=datetime.now())
			registro1.save()
			registro.save()
			messages.success(request, 'Pregunta Creada Exitosamente(puede ingresar mas preguntas)')
		return render(request,'prueba/preguntas.html')
	else:
		messages.error(request, 'Esta Prueba se Encuentra Desactivada Activela Para Gestionarla.')
		return redirect('gesp')

#FUNCION QUE EDITA LAS PREGUNTAS DE DE UNA DETERMINADA PRUEBA

def e_pre(request, cod_pregunta):
	query=preguntas.objects.get(cod_pregunta=cod_pregunta)
	usr_act=request.user
	usrb='Se Modifico la Pregunta #{1} de la prueba #{0}'.format(query.cod_p_id, query.cod_pregunta) 
	if request.method == 'GET':
		form = preguntaform(instance=query)
	else:
		form = preguntaform(request.POST, instance=query)
		if form.is_valid():
			form.save()
			registro = UserLog(usuario=usr_act , accion=usrb, modulo='Modificar preguntas', sesion='no_aplica', fecha_hora=datetime.now())
			registro.save()
			messages.success(request, 'Datos Modificados Satisfactoriamente')	
			return redirect('gesp')
	return render(request, 'prueba/e_peg.html', {'object':form })

#FUNCION QUE MUESTRA LAS PRUEBAS CORRESPONDIENTES A UNA DETERMINADA PREGUNTA

def v_preg(request, cod_prueba):
	usu_act=request.user
	query = preguntas.objects.filter(cod_p_id=cod_prueba)
	context = {'obj_pre':query}
	registro = UserLog(usuario=usu_act.username , accion='listo preguntas', modulo='prueba/ver_preguntas', sesion='no_aplica', fecha_hora=datetime.now())
	registro.save()
	return render(request, 'prueba/ver_preguntas.html', context)


#FUNCION QUE ELIMINA LAS PREGUNTAS DE LAS PRUEBAS


class eli_pre(SuccessMessageMixin, DeleteView):
	model = preguntas
	template_name = 'prueba/eli_p.html'
	success_url = reverse_lazy('gesp')
	success_message='Pregunta Eliminada'


#FUNCION QUE MUESTRA LAS PRUEBAS 


def v_pru(request, cod_prueba):
	query = prueba.objects.get(cod_prueba=cod_prueba)
	query2 = preguntas.objects.filter(cod_p_id=cod_prueba)

	if query.activa == True:
		context_dict = {'obj_pru':query ,'obj_pre':query2}
		return render(request, 'prueba/prueba.html', context_dict)
	else:
		messages.error(request, 'Esta Prueba se Encuentra Desactivada.')
		return redirect('gesp')


#FUNCION QUE ESTRUCTURA LAS PRUEBAS PARA LOS ESTUDIANTES

def v_pru_e(request, cod_prueba):
	query = prueba.objects.get(cod_prueba=cod_prueba)
	query2 = preguntas.objects.filter(cod_p_id=cod_prueba) 
	query3 = preguntas.objects.filter(cod_p_id=cod_prueba).count()
	query4 = User.objects.get(ci=request.user.ci)
	if request.method == 'GET':
		if query.activa == True:
			context_dict = {'obj_pru':query ,'obj_pre':zip(query2, range(query3))}
			return render(request, 'prueba/prueba_e.html', context_dict)
		elif request.user.tipo_usuario != "Estudiante":
			messages.error(request, 'Esta Prueba se Encuentra Desactivada.')
			return redirect('gesp')
		else:
			messages.error(request, 'Esta Prueba se Encuentra Desactivada.') 
			return redirect('ver_p_es')
	else:
		query5 = solucionex.objects.filter(Q(cod_pru=cod_prueba) & Q(ci_e = request.user.ci))
		if query5.exists():
			messages.error(request, 'No puedes Volver a presentar el Examen Comunicate con tu profesor')
			return redirect('ver_p_es')
		else:
			registro = solucionex(cod_pru = query, ci_e = query4)
			registro.save()
			query6 = solucionex.objects.get(Q(cod_pru=cod_prueba) & Q(ci_e = request.user.ci))
			notae = 0
			for i in range(query3):
				registro1 = solucionpr(ci_e = query4, cod_examen=query6, ponderacion = request.POST['pon_{0}'.format(i)], pregunta=request.POST['pre_{0}'.format(i)] , respuesta=request.POST['r_{0}'.format(i)] )
				registro1.save()
				query7 = preguntas.objects.get(pregunta=registro1.pregunta)
				query8 = solucionpr.objects.get(Q(pregunta=query7.pregunta) & Q(ci_e = request.user.ci))
				if query8.respuesta == query7.rc:
					notae = notae+query7.ponderacion
			messages.success(request, 'Has Obtenido {0}puntos en la Prueba.'.format(notae))
			registro2 = nota(ci_e = query4, cod_p=query, nota='{0}'.format(notae), fecha=datetime.now())
			registro2.save()
			return redirect('ver_p_es')
	return render(request, 'prueba/list_pru.html')

#FUNCION QUE ACTIVA Y DESACTIVA LAS PRUEBAS

def act_dct(request, cod_prueba):
	
	act=prueba.objects.get(cod_prueba=cod_prueba)
	usr_act=request.user
	usrb='Se Desactivo la Prueba' 
	usrb1='Se Activo la Prueba'

	if act.activa == True:
		act.activa = False
		registro = UserLog(usuario=usr_act.username , accion=usrb, modulo='prueba/act/dct', sesion='no_aplica', fecha_hora=datetime.now())
		registro.save()
		act.save()
		messages.warning(request, 'Prueba Desactivada')
	else:
		act.activa = True
		act.save()
		registro = UserLog(usuario=usr_act.username , accion=usrb1, modulo='prueba/act/dct', sesion='no_aplica', fecha_hora=datetime.now())
		registro.save()
		messages.success(request, 'Prueba Activada')
	return redirect('gesp')

# BITACORA

class lisbi(ListView):
	queryset = UserLog.objects.order_by('-id')
	template_name = 'bitacora/bitacora.html'
	paginate_by = 8

# SIMULACION 

def sim(request):
	if User.is_authenticated:
		username = request.user
		registro = UserLog(usuario=username, accion='entrada a modulo Simulacion', modulo='Simulacion', sesion='no_aplica', fecha_hora=datetime.now())
		registro.save()
	return render(request, 'simulacion/simulacion.html')

def mosnotas(request, cod_prueba):
	query = nota.objects.filter(cod_p=cod_prueba)
	contexto = {'object_list':query}
	paginate_by = 8
	return render(request, 'prueba/notas.html', contexto)
