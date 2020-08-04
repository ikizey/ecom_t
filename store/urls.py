from django.urls import path

from .views import store, cart

urlpatterns = [
    path('', store, name="home"),
    path('cart', cart, name="cart"),
]
