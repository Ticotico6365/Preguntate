# Generated by Django 4.2.15 on 2024-08-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PreguntasApp', '0003_pregunta_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
