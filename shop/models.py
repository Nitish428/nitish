from django.db import models

# Create your models here.

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
         return f"{self.name} ({self.email})"
    
    #user:Nitish
    #password:Nkg1234@
   