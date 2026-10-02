from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_GROSSISTE = 'GROSSISTE'
    ROLE_DETAILLANT = 'DETAILLANT'
    ROLE_CHOICES=[ 
        (ROLE_GROSSISTE, 'Grossiste'),
        (ROLE_DETAILLANT, 'Détaillant'),
    ]

    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role=models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_DETAILLANT)
    nom_commercial=models.CharField(max_length=100, blank=True)
    telephone=models.CharField(max_length=20, blank=True)
    adresse=models.EmailField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"