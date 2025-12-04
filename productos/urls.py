# productos/urls.py

from django.urls import path
from . import views

# Define un nombre de espacio para estas URLs. Evita conflictos con URLs de otras apps.
app_name = 'productos'

# --- RUTAS WEB ---
web_urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('<slug:categoria_slug>/', views.lista_productos, name='lista_productos_por_categoria'),
    path('<int:id>/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
    path('agregar-carrito-simple/<int:product_id>/', views.add_to_cart_simple, name='agregar-carrito-simple'),
]

# --- RUTAS API ---
api_urlpatterns = [
    path('api/products/', views.ProductoListAPIView.as_view(), name='api_products'),
]

# --- INCLUYE AMBAS EN urlpatterns ---
urlpatterns = web_urlpatterns + api_urlpatterns

# API REST para productos (solo JSON)
urlpatterns_api = [
    path('', views.ProductoListAPIView.as_view(), name='api_products'),
]