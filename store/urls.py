from django.urls import path

from .views import add_to_cart, store, cart, item

urlpatterns = [
    path('', store, name="home"),
    path('cart', cart, name="cart"),
    path('items/<int:pk>/', item, name="item"),
    path('items/<int:item_pk>/add_to_cart', add_to_cart, name="add_to_cart"),
]
