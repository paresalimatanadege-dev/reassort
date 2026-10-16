from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from .models import Product


@login_required
@role_required('GROSSISTE')
def product_list(request):
    products = Product.objects.filter(wholesaler=request.user).order_by('nom')
    return render(request, 'wholesaler/products.html', {'products': products})