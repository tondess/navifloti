from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from sistem.views import *
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
# url del admin de django

    url(r'^admin/', include(admin.site.urls)),

# url de inicio
	
    url(r'^accounts/login/', user_login, name='login'),
    url(r'^inicio/$', login_required(inicio.as_view()), name='home'),

# url de salida
	
	url(r'^logout/', logout_then_login, name='logout'),

# url de perfil

    url(r'^perfil_usuario/$', login_required(perfil), name='perfil'),

# urls de gestion de usuario

	url(r'^usuario/c_usr/$', cu, name='vista1'),
    url(r'^usuario/l_usr/$', login_required(lusu.as_view()), name='vista2'),
	url(r'^usuario/m_usr/(?P<ci>\d+)/$', login_required(modu), name='vista3'),
	url(r'^usuario/e_usr/(?P<ci>\d+)/$', login_required(act_dct_usu), name='vista4'),
	url(r'^usuario/c_contra/$', login_required(camb_contra), name='c_contra'),
 
# urls de pruebas

	url(r'^pruebas/registrar_prueba/$', login_required(cp.as_view()), name='crearp'),
	url(r'^pruebas/gestionar_pruebas/$', login_required(lp), name='gesp'),
	url(r'^pruebas/ver_pruebas/$', login_required(lpda.as_view()), name='ver_p_es'),
	url(r'^pruebas/mod_prueba/(?P<pk>\d+)/$', login_required(modp.as_view()), name='modp'),
	url(r'^pruebas/act/(?P<cod_prueba>\d+)/$', login_required(act_dct), name='act_dct'),
	url(r'^pruebas/registrar_preguntas/(?P<cod_prueba>\d+)/$', login_required(c_pre), name='c_preg'),
	url(r'^pruebas/editar_pregunta/(?P<cod_pregunta>\d+)/$', login_required(e_pre), name='e_preg'),
	url(r'^pruebas/eliminar_pregunta/(?P<pk>\d+)/$', login_required(eli_pre.as_view()), name='eli_p'),
	url(r'^pruebas/ver_prueba/(?P<cod_prueba>\d+)/$', login_required(v_pru), name='v_pru'),
	url(r'^pruebas/ver_preguntas/(?P<cod_prueba>\d+)/$', login_required(v_preg), name='v_preg'),

	url(r'^pruebas/ver_prueba_estudiante/(?P<cod_prueba>\d+)/$', login_required(v_pru_e), name='v_pru_e'),
	url(r'^pruebas/ver_notas_estudiante/(?P<cod_prueba>\d+)/$', login_required(mosnotas), name='v_not_e'),

#	url(r'^pruebas/resultados/$', login_required(eva_pru), name='evalu'),


#url de bitacora pruebas/g_pruebas

	url(r'^bitacora/$', login_required(lisbi.as_view()), name='listbi'), 

# url de simulacion

	url(r'^simulador/$', login_required(sim), name='sim'),

]
