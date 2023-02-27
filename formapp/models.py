from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=50, default='')
    phone = models.CharField(max_length=11, default='')
    message = models.CharField(max_length=200, default='')
    def __str__(self):
        return [self.name, self.email, self.phone, self.message]