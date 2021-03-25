from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    billing = models.BooleanField(verbose_name='', default=False,)
    
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'