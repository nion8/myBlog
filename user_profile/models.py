from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField('username', max_length=23, unique=True, db_index=True)
    email = models.EmailField('email adress', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    #
    #  def __unicode__(self):
    #      return self.username
