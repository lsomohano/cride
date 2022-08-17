"""User model."""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser

#Utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """User models
    
    Extend from Django's Abstract USer, Change the username field
    to email and add some extra abstrack"""

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'inique':'A user with that email alredy exists.'
        }
    )

    phone_number = models.CharField(max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name','last_name'] 

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text='Set to true when the user have verified its email addres.'
    )   
