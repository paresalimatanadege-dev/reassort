from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('mes-produits/', views.product_list, name='product_list'),
    path('mes-produits/ajouter/', views.product_create, name='product_create'),
    path('mes-produits/<int:pk>/modifier/', views.product_update, name='product_update'),
]