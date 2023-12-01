from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=500)


    def __str__(self) -> str:
        return self.title
    

