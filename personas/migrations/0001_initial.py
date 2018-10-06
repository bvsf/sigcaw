# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-06 18:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localidades', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuartelero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='cuarteleros', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DireccionElectronica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(choices=[('P', 'Particular'), ('L', 'Laboral')], default='P', max_length=255, verbose_name='Uso')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Obervaciones')),
                ('mail', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Direccion de Email',
                'verbose_name_plural': 'Direcciones de Email',
            },
        ),
        migrations.CreateModel(
            name='DireccionPostal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(choices=[('P', 'Particular'), ('L', 'Laboral')], default='P', max_length=255, verbose_name='Uso')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Obervaciones')),
                ('calle', models.CharField(max_length=255, verbose_name='Calle')),
                ('numero', models.SmallIntegerField(verbose_name='Número')),
                ('piso', models.CharField(blank=True, max_length=5, null=True, verbose_name='Piso')),
                ('departamento', models.CharField(blank=True, max_length=5, null=True, verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Dirección Postal',
                'verbose_name_plural': 'Direcciones Postales',
            },
        ),
        migrations.CreateModel(
            name='DireccionWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(choices=[('P', 'Particular'), ('L', 'Laboral')], default='P', max_length=255, verbose_name='Uso')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Obervaciones')),
                ('direccion', models.URLField(verbose_name='Dirección Web')),
                ('tipo', models.CharField(choices=[('S', 'Perfil Web Social'), ('L', 'Pagina Web Laboral')], default='S', max_length=255, verbose_name='Tipo web')),
            ],
            options={
                'verbose_name': 'Dirección Web',
                'verbose_name_plural': 'Direcciones Web',
            },
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cuit', models.CharField(choices=[('CUIT', 'CUIT'), ('CUIL', 'CUIL')], default='CUIT', max_length=4, verbose_name='CUIT/CUIL')),
                ('nro_cuit', models.CharField(blank=True, max_length=13, null=True, verbose_name='Numero de CUIT/CUIL')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(choices=[('P', 'Particular'), ('L', 'Laboral')], default='P', max_length=255, verbose_name='Uso')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Obervaciones')),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Teléfono')),
                ('tipo', models.CharField(choices=[('C', 'Celular'), ('F', 'Fijo')], default='C', max_length=255, verbose_name='Tipo de Teléfono')),
            ],
            options={
                'verbose_name': 'Teléfono',
                'verbose_name_plural': 'Teléfonos',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('entidad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Entidad')),
                ('razon_social', models.CharField(max_length=255, verbose_name='Razón Social')),
            ],
            options={
                'verbose_name': 'Institución',
                'verbose_name_plural': 'Instituciones',
            },
            bases=('personas.entidad',),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('entidad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Entidad')),
                ('apellido', models.CharField(max_length=255, verbose_name='Apellido')),
                ('primer_nombre', models.CharField(max_length=255, verbose_name='Primer Nombre')),
                ('segundo_nombre', models.CharField(blank=True, max_length=255, null=True, verbose_name='Segundo Nombre')),
                ('tercer_nombre', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tercer Nombre')),
                ('tipo_documento', models.CharField(choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE')], default='DNI', max_length=10, verbose_name='Tipo de Documento')),
                ('documento', models.CharField(max_length=11, unique=True, verbose_name='Número de documento')),
                ('grupo_sanguineo', models.CharField(blank=True, choices=[('AB', 'Grupo AB'), ('A', 'Grupo A'), ('B', 'Grupo B'), ('O', 'Grupo O')], default='AB', max_length=255, null=True, verbose_name='Grupo Sanguíneo')),
                ('factor_sanguineo', models.CharField(blank=True, choices=[('+', 'RH+'), ('-', 'RH-')], default='+', max_length=255, null=True, verbose_name='Factor Sanguíneo')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('fecha_desceso', models.DateField(blank=True, null=True, verbose_name='Fecha de Fallecimiento')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=255, verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['apellido', 'primer_nombre'],
            },
            bases=('personas.entidad',),
        ),
        migrations.AddField(
            model_name='telefono',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entidad_telefono', to='personas.Entidad'),
        ),
        migrations.AddField(
            model_name='direccionweb',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entidad_direccionweb', to='personas.Entidad'),
        ),
        migrations.AddField(
            model_name='direccionpostal',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entidad_direccionpostal', to='personas.Entidad'),
        ),
        migrations.AddField(
            model_name='direccionpostal',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localidad', to='localidades.Localidad', verbose_name='Localidad'),
        ),
        migrations.AddField(
            model_name='direccionelectronica',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entidad_direccionelectronica', to='personas.Entidad'),
        ),
        migrations.AddField(
            model_name='cuartelero',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cuarteleros', to='personas.Persona', verbose_name='Persona'),
        ),
    ]
