from django.db import models


from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    modified = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)