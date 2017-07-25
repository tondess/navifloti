# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, unique=True)),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('ci', models.IntegerField(serialize=False, primary_key=True)),
                ('tipo_usuario', models.CharField(max_length=20)),
                ('esp', models.CharField(max_length=20)),
                ('groups', models.ManyToManyField(related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', verbose_name='groups', related_name='user_set', blank=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', help_text='Specific permissions for this user.', to='auth.Permission', verbose_name='user permissions', related_name='user_set', blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='bitacora',
            fields=[
                ('cod_acc', models.AutoField(serialize=False, primary_key=True)),
                ('accion', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='fluidos',
            fields=[
                ('cod_f', models.AutoField(serialize=False, primary_key=True)),
                ('login', models.CharField(max_length=200)),
                ('nombre_f', models.CharField(max_length=200)),
                ('g_e', models.DecimalField(max_digits=5, decimal_places=2)),
                ('p_e', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='materiales',
            fields=[
                ('cod_m', models.AutoField(serialize=False, primary_key=True)),
                ('login', models.CharField(max_length=200)),
                ('nombre_m', models.CharField(max_length=200)),
                ('g_e', models.DecimalField(max_digits=5, decimal_places=2)),
                ('p_e', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='preguntas',
            fields=[
                ('cod_pregunta', models.AutoField(serialize=False, primary_key=True)),
                ('ponderacion', models.IntegerField()),
                ('pregunta', models.CharField(max_length=200)),
                ('r1', models.CharField(max_length=200)),
                ('r2', models.CharField(max_length=200)),
                ('r3', models.CharField(max_length=200)),
                ('r4', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='prueba',
            fields=[
                ('cod_prueba', models.AutoField(serialize=False, primary_key=True)),
                ('valor', models.IntegerField()),
                ('seccion', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=20)),
                ('Duracion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='solucionex',
            fields=[
                ('cod_prueba', models.AutoField(serialize=False, primary_key=True)),
                ('cod_ex', models.IntegerField()),
                ('ponderacion', models.IntegerField()),
                ('seccion', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=20)),
                ('Duracion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='solucionpr',
            fields=[
                ('cod_respuesta', models.AutoField(serialize=False, primary_key=True)),
                ('ponderacion', models.IntegerField()),
                ('pregunta', models.CharField(max_length=200)),
                ('respuesta', models.CharField(max_length=200)),
                ('cod_examen', models.ForeignKey(to='sistem.solucionex', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('ciw', models.IntegerField(serialize=False, primary_key=True)),
                ('tipow_usuario', models.CharField(max_length=20)),
                ('espw', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='solucionex',
            name='ci_e',
            field=models.ForeignKey(to='sistem.usuario', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='prueba',
            name='ci_p',
            field=models.ForeignKey(to='sistem.usuario', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='cod_p',
            field=models.ForeignKey(to='sistem.prueba', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='materiales',
            name='admm',
            field=models.ForeignKey(to='sistem.usuario', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fluidos',
            name='adm',
            field=models.ForeignKey(to='sistem.usuario', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='ci_u',
            field=models.ForeignKey(to='sistem.usuario', null=True, blank=True),
        ),
    ]
