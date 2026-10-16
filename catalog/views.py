from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
@role_required('GROSSISTE')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk, wholesaler=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit modifié.")
            return redirect('catalog:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'wholesaler/product_form.html',
                  {'form': form, 'titre': 'Modifier le produit'})