from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    USER_TYPES = (
        ("SUPER ADMIN", "SUPER ADMIN"),
        ("ADMIN", "ADMIN"),
        ("USER", "USER")
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

class BaseClass(models.Model):
    """
    BaseClass will be inherited by other models in place of models.Model.
    It has updated_at, creatted_at and active_status which are required 
    by all other models.
    """
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active_status = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class Vehicle(BaseClass):
    vehicle_number = models.CharField(max_length=20)
    VEHICLE_OPTIONS = (
        ("TWO", "TWO"), 
        ("THREE", "THREE"), 
        ("FOUR WHEELER", "FOUR WHEELER")
    )
    vehicle_option = models.CharField(max_length=15,choices=VEHICLE_OPTIONS)
    modal = models.TextField()
    description =models.TextField()

    def __str__(self):
        return self.vehicle_number