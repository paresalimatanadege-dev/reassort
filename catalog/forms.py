from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nom', 'description', 'prix', 'unite', 'disponible']

    def clean_prix(self):
        prix = self.cleaned_data['prix']
        if prix <= 0:
            raise forms.ValidationError("Le prix doit être supérieur à zéro.")
        return prix