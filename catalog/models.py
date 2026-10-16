from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    wholesaler = models.ForeignKey(User, on_delete=models.PROTECT, related_name='products')
    nom = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    unite = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom