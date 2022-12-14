from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):

        return self.first_name
