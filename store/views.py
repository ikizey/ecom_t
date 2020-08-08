"""Views for store app:
HomePageView: main view
ItemPageView: each product view
cart: cart view
add_to_cart: used to add items to cart.

get_banners: util function (not a view)
"""
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from .models import Banner, Item, Order, OrderItem


def get_banners():
    """Provides banners for contexts in views

    Returns:
        QuerySet of all banners.
    """
    return Banner.objects.all()


class HomePageView(TemplateView):
    """Main page."""

    template_name = 'store/store.html'

    def get_context_data(self, **kwargs):
        """ Provides context data for template:
        All active products. -> Item.objects.filter(is_active=True)
        Also banners. -> get_banners()
        """
        context = super().get_context_data(**kwargs)
        context['banners'] = get_banners()
        context['items'] = Item.objects.filter(is_active=True)
        return context


class ItemPageView(TemplateView):
    """Page for each product(item)."""

    template_name = 'store/item.html'

    def get_context_data(self, **kwargs):
        """ Provides context data for template:
        All data about current product. -> Item.objects.get(pk=kwargs['pk'], is_active=True)
        Also banners. -> get_banners()
        """
        context = super().get_context_data(**kwargs)
        context['banners'] = get_banners()
        context['item'] = Item.objects.get(pk=kwargs['pk'], is_active=True)
        return context


def cart(request):
    """Cart view."""
    user = request.user
    # Redirect non authenticated user to login page.
    if user.is_anonymous:
        return redirect('login')

    template = 'store/cart.html'

    # Context data for template:
    # All ordered items of current user.
    # Creates new order if non complete order not exists.
    order, _ = Order.objects.get_or_create(customer=user, complete=False)
    items = order.order_item.all()

    context = {'items': items}

    return render(request, template, context)


def add_to_cart(request, item_pk):
    """Add to card view.
    ! Never shown to user ! Redirects to product page with pk=item_pk
    Used to save products(items) to cart of current user
    """
    user = request.user
    # Do no save data for  anonymous users
    # Redirect non authenticated user to login page.
    if user.is_anonymous:
        return redirect('login')

    # Context data for template:
    # get product(item) by pk
    try:
        product = Item.objects.get(pk=item_pk, is_active=True)
    except Item.DoesNotExist:
        # meaning product was deleteed while user was on product page.
        # so can't sand back to it's page
        return redirect('home')
    order, _ = Order.objects.get_or_create(customer=user, complete=False)
    order_item, _ = OrderItem.objects.get_or_create(order=order, item=product)

    order_item.save()

    # Redirect to product page with pk=item_pk
    return redirect('item', item_pk)
