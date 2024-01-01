from django.db import models

# Create your models here.

class Task(models.Model):
    titre=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    statut=models.BooleanField(default=False)
    
    def __str__(self):
        return self.titre