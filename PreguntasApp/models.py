from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.pregunta_text