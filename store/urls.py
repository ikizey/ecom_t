from django.urls import path

from .views import HomePageView, ItemPageView, add_to_cart, cart

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('items/<int:pk>/', ItemPageView.as_view(), name="item"),
    path('cart', cart, name="cart"),
    path('cart/add_item/<int:item_pk>/', add_to_cart, name="add_to_cart"),
]
