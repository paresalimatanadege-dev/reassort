from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from accounts.decorators import role_required
from .forms import ProductForm
from .models import Product
from django.db.models import ProtectedError

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

@login_required
@role_required('GROSSISTE')
@require_POST
def product_toggle(request, pk):
    product = get_object_or_404(Product, pk=pk, wholesaler=request.user)
    product.disponible = not product.disponible
    product.save()
    return redirect('catalog:product_list')

@login_required
@role_required('GROSSISTE')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, wholesaler=request.user)
    if request.method == 'POST':
        try:
            product.delete()
        except ProtectedError:
            messages.error(request, "Ce produit figure dans des commandes : il ne peut pas être supprimé. Rendez-le indisponible à la place.")
        else:
            messages.success(request, "Produit supprimé.")
        return redirect('catalog:product_list')
    return render(request, 'wholesaler/product_confirm_delete.html', {'product': product})