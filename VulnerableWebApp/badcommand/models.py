from django.db import models

# Create your models here.
class Command(models.Model):
    command_text = models.CharField(max_length=200)
    def __str__(self):
        return self.command_text
