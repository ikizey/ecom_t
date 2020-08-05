from django.shortcuts import render
from .models import Banner, Item


def get_banners():
    return Banner.objects.all()


def store(request):
    template = 'store/store.html'

    banners = get_banners()
    items = Item.objects.filter(is_active=True)

    context = {'banners': banners, 'items': items}
    return render(request, template, context)


def item(request, pk):
    template = 'store/item.html'

    banners = get_banners()
    item = Item.objects.get(pk=pk, is_active=True)

    context = {'banners': banners, 'item': item}
    return render(request, template, context)


def cart(request):
    return render(request, 'store/cart.html')

