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
        items: All active products.
        banners : Banners.
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
        item : Data about current product.
        banners : Banners.
        """
        context = super().get_context_data(**kwargs)
        context['banners'] = get_banners()
        try:
            context['item'] = Item.objects.get(pk=kwargs['pk'], is_active=True)
        except Item.DoesNotExist:
            # meaning product was deleted or set inactive while user was on the page.
            return redirect('home')
        return context


def cart(request):
    """Cart view."""
    user = request.user
    # Redirect non authenticated user to login page.
    if user.is_anonymous:
        return redirect('login')

    template = 'store/cart.html'

    # Context data for template:
    # Creates new cart(order) if non-complete order does not exist.
    cart, _ = Order.objects.get_or_create(customer=user, complete=False)
    # grab all items from order
    items = cart.order_item.all()

    context = {'items': items}

    return render(request, template, context)


def add_to_cart(request, item_pk):
    """Add to card view.
    ! Never shown to user ! Redirects to product page with pk=item_pk
    Used to save products(items) to cart(order) of current user
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
        # meaning product was deleted  or set inactive while user was on product page.
        # so can't sand back to it's page
        return redirect('home')
    cart, _ = Order.objects.get_or_create(customer=user, complete=False)
    order_item = OrderItem.objects.create(order=cart, item=product)

    order_item.save()

    # Redirect to product page with pk=item_pk
    return redirect('item', item_pk)


def del_from_cart(request, order_item_pk):
    """Remove to card view.
    ! Never shown to user ! Redirects to cart
    Used to delete product(item) from cart(order) of current user
    """
    user = request.user
    if user.is_authenticated:
        try:
            product = OrderItem.objects.get(pk=order_item_pk)
        except Item.DoesNotExist:
            # if prevously deleted. in another tab, for example
            pass
        else:
            # check if item belongs to user's order
            if product.order.customer == user:
                product.delete()

    return redirect('cart')

