# Generated by Django 4.2.5 on 2023-10-22 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('detalle', models.TextField()),
                ('detalle_corto', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('S', 'Suspensión de actividades'), ('C', 'Suspención de clase'), ('I', 'Información')], max_length=1)),
                ('visible', models.BooleanField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comunicados.entidad')),
                ('publicado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
