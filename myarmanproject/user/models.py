from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
  username = models.CharField(max_length = 50, blank=False, unique = True)
  password = models.CharField(max_length = 10, blank=False, unique = True)
  phone_no = models.CharField(max_length = 11)
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['first_name', 'last_name']
  def __str__(self):
      return "{}".format(self.username)
  
  def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.password:
            self.set_password(self.password)

        super().save(*args, **kwargs)