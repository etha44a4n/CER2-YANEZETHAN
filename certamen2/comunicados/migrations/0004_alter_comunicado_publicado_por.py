# Generated by Django 4.2.5 on 2023-10-21 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comunicados', '0003_comunicado_publicado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='publicado_por',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]