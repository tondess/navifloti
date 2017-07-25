from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from sistem.models import User

password1=""

def pass2(value):
   
    password2 = value
    
    if password1 and password2 and password1 != password2:
        raise ValidationError(_('Las Contraseñas No Coinciden'))


def pass_str(value):
    """  valida que la contraseña contenga almenos 8 digitos incluyendo letras y numeros """
    min_length = 8
    global password1
    password1 = value

    if len(value) < min_length:
        raise ValidationError(_('La Contraseña Debe Tener al Menos {0} Caracteres').format(min_length))

    if not any(char.isdigit() for char in value):
        raise ValidationError(_('Debe Contener al Menos 1 Numero'))

    if not any(char.isalpha() for char in value):
        raise ValidationError(_('Debe Contener al Menos 1 Letra'))


def ci_val(value):
    """  valida que la cedula contenga almenos 5 digitos y maximo 8 incluyendo solo numeros """
    min_length = 5
    max_length = 8

    ci_dupli = User.objects.filter(ci=value)

    if len(str(value)) < min_length:
        raise ValidationError(_('La cédula debe tener al menos {0} caracteres').format(min_length))
    
    if len(str(value)) > max_length:
        raise ValidationError(_('La cédula debe tener maximo {0} caracteres').format(max_length))
    
    if ci_dupli.exists():
        raise ValidationError(_('Cédula ya esta registrada'))

    if any(char.isalpha() for char in str(value)):
        raise ValidationError(_('No puede contener letras'))

