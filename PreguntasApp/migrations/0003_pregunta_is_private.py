# Generated by Django 4.2.15 on 2024-08-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PreguntasApp', '0002_usuario_is_active_usuario_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
