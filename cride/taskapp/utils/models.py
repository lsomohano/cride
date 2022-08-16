"""Django models utilities."""

#Django
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model.
    
    CRideModel acts as an abstract base class from whitch every
    other model in the project will inherit. This class porvides
    every tablet with the following attributes:
        + created (DateTime): Store the datetime the objects was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified'
    )

    class Meta:
        """Meta option."""

        asbtract = True

        get_latest = 'created'
        ordering = ['-created', '-modified']
