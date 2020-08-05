from django.shortcuts import render
from .models import Banner, Item


def store(request):
    template = 'store/store.html'

    banners = Banner.objects.all()
    items = Item.objects.filter(is_active=True)

    context = {'banners': banners, 'items': items}
    return render(request, template, context)


def cart(request):
    return render(request, 'store/cart.html')
