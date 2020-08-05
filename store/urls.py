from django.urls import path

from .views import store, cart, item

urlpatterns = [
    path('', store, name="home"),
    path('cart', cart, name="cart"),
    path('items/<int:pk>/', item, name="item"),
]
