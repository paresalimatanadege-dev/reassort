from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from .forms import ProductForm
from .models import Product

@login_required
@role_required('GROSSISTE')
def product_list(request):
    products = Product.objects.filter(wholesaler=request.user).order_by('nom')
    return render(request, 'wholesaler/products.html', {'products': products})

@login_required
@role_required('GROSSISTE')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.wholesaler = request.user
            product.save()
            messages.success(request, "Produit ajouté.")
            return redirect('catalog:product_list')
    else:
        form = ProductForm()
    return render(request, 'wholesaler/product_form.html',
                  {'form': form, 'titre': 'Ajouter un produit'})