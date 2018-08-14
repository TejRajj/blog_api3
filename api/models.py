from django.db import models

# Create your models here.
class Login(models.Model):
    Full_name = models.CharField(max_length=20)
    Country = models.CharField(max_length=20)

    def __str__(self):
        return (self.id, self.Full_name)