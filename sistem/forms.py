from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from sistem.models import *
from sistem.validators import *
from django.core.exceptions import ValidationError

class usrform(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(usrform, self).__init__(*args, **kwargs)
		self.fields['password1'].validators.append(pass_str)
		self.fields['password2'].validators.append(pass2)
		self.fields['ci'].validators.append(ci_val)

	class Meta:
		model = User
		
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',			
				'ci', 
			    'tipo_usuario',
			    'esp', 
			]
		labels = {
				'username': 'Usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellido',
				'email': 'Correo',
				'ci': 'Cedula',
				'tipo_usuario': 'Tipo de usuario',
				'esp': 'especialidad',
			}
		widgets = {
				'username': forms.TextInput(attrs={'required': True, 'class':'form-control', 'minlength': '5','maxlength': '25'}), 
				'first_name': forms.TextInput(attrs={ 'required': True, 'class':'form-control', 'minlength': '5','maxlength': '25'}), 
				'last_name': forms.TextInput(attrs={ 'required': True, 'class':'form-control', 'minlength': '5','maxlength': '25'}),
				'email': forms.EmailInput(attrs={ 'required': True, 'class':'form-control'}),
				'ci': forms. NumberInput(attrs={ 'required': True, 'class':'form-control'}),
				'tipo_usuario': forms.TextInput(attrs={ 'required': True, 'class':'form-control'}),
				'esp': forms.TextInput(attrs={ 'required': True, 'class':'form-control'}),
			}

class modusrform(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(modusrform, self).__init__(*args, **kwargs)
		self.fields['password1'].validators.append(pass_str)
		self.fields['password2'].validators.append(pass2)
		
	class Meta:
		model = User
		
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',			
				'ci', 
			    'tipo_usuario',
			    'esp', 
			]
		labels = {
				'username': 'Usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellido',
				'email': 'Correo',
				'ci': 'Cedula',
				'tipo_usuario': 'Tipo de usuario',
				'esp': 'especialidad',
			}
		widgets = {
				'username': forms.TextInput(attrs={'required': True, 'class':'form-control', 'minlength': '5','maxlength': '25'}),
				'first_name': forms.TextInput(attrs={ 'required': True, 'class':'form-control', 'minlength': '5','maxlength': '25'}),
				'last_name': forms.TextInput(attrs={ 'required': True, 'class':'form-control', 'minlength': '5','maxlength': '25'}),
				'email': forms.EmailInput(attrs={ 'required': True, 'class':'form-control'}),
				'ci': forms. NumberInput(attrs={ 'required': True, 'class':'form-control', 'readonly': True,}),
				'tipo_usuario': forms.TextInput(attrs={ 'required': True, 'class':'form-control'}),
				'esp': forms.TextInput(attrs={ 'required': True, 'class':'form-control'}),
			}


class camb_c(PasswordChangeForm):
	
	def __init__(self, *args, **kwargs):
		super(camb_c, self).__init__(*args, **kwargs)

		self.fields['new_password1'].validators.append(pass_str)
		self.fields['new_password2'].validators.append(pass2)

	class Meta:
		model = User	
		
		fields = [
			'old_password',
			'new_password1',
			'new_password2',
		]


class pruebaform(forms.ModelForm):

	class Meta:
		model = prueba
		
		fields = [
			'ci_p', 
		    'valor',
		    'titulo',
		    'seccion',
		    'fecha',
		    'hora',
		    'Duracion',
			]
		labels = {
			'ci_p': 'Cedula del Profesor',
			'valor': 'Ponderacion del Examen',
			'titulo': 'Titulo',
			'seccion': 'Seccion',
			'fecha': 'Fecha',
			'hora': 'Hora',
			'Duracion': 'Duracion del Examen',
			}

class preguntaform(forms.ModelForm):

	class Meta:
		model = preguntas
		
		fields = [
			'cod_pregunta',
		    'ponderacion', 
		    'pregunta',
		    'r1',
		    'r2',
		    'r3',
			'r4',
			'rc',
			]