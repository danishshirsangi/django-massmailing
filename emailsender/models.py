from django.db import models

# Create your models here.

class EmailCsvModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    file_hold = models.FileField()

    def __str__(self) -> str:
        return self.name
    
