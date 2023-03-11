from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=False)
    mobile_no = models.PositiveIntegerField(unique=True, blank=False)


    def __str__(self):
        return self.email

class Customer(models.Model):
    profile_number = models.PositiveIntegerField(blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)