from django.shortcuts import render, redirect
from .models import Banner, Item, Order, OrderItem


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


def add_to_cart(request, item_pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')

    product = Item.objects.get(pk=item_pk, is_active=True)
    order, _ = Order.objects.get_or_create(customer=user, complete=False)
    order_item, _ = OrderItem.objects.get_or_create(order=order, item=product)

    order_item.save()

    return redirect('item', item_pk)


def cart(request):
    return render(request, 'store/cart.html')
