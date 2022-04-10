from django.db import models

# Create your models here.

class EmailCsvModel(models.Model):
    name = models.CharField(max_length=20)
    file_hold = models.FileField()

    def __str__(self) -> str:
        return self.name
    
