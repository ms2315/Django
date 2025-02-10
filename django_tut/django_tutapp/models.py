from django.db import models
from django.contrib.auth.models import AbstractUser    # For custo User Model 
from .managers import MyUserManager   # For custo User Model

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)

# Create your models here.
class MyUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    
    '''
    Here you assign custom user manager
    '''
    objects = MyUserManager()
    admin_objects = models.Manager() 

    '''
    Here we can add custo username field and require fields
    '''
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = []
    
    
    def __str__(self):
        return self.username
    
    
class Student(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    roll_no = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name