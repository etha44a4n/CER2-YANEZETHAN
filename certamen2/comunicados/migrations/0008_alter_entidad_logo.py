# Generated by Django 4.2.5 on 2023-10-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunicados', '0007_alter_entidad_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='logo',
            field=models.ImageField(upload_to=''),
        ),
    ]
