from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from .models import Banner, Item, Order, OrderItem


def get_banners():
    return Banner.objects.all()


class HomePageView(TemplateView):
    template_name = 'store/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = get_banners()
        context['items'] = Item.objects.filter(is_active=True)
        return context


class ItemPageView(TemplateView):
    template_name = 'store/item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = get_banners()
        context['item'] = Item.objects.get(pk=kwargs['pk'], is_active=True)
        return context


def cart(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')

    template = 'store/cart.html'

    order, _ = Order.objects.get_or_create(customer=user, complete=False)
    items = order.order_item.all()

    context = {'items': items}

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
