from django.conf import settings
from django.db import models
from django.urls import reverse


class Brand(models.Model):
    """Brand field for items(products)"""

    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Item(models.Model):
    """Product model"""

    fullname = models.CharField(max_length=500)
    description = models.TextField(max_length=1000, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField(default=0)  # в копейках
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='brand'
    )

    image = models.ImageField(
        default='items_images/default.jpg', upload_to='items_images'
    )

    def __str__(self):
        return self.fullname

    # returns price in rubles
    @property
    def rub_price(self):
        return self.price / 100

    @rub_price.setter
    def set_rub_price(self, price_in_rub):
        self.price = price_in_rub * 100

    def get_absolute_url(self):
        return reverse('item', args=[str(self.id)])


class Banner(models.Model):
    """Banners for pages"""

    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner_images')

    def __str__(self):
        return self.description


class Order(models.Model):
    """Customer Orders
    Non-complete order is cart, otherwise some past order.
    """

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='order',
    )
    ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f"Order of {self.customer.username} on {self.ordered}"


class OrderItem(models.Model):
    """Model for items in orders"""

    item = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True, related_name='order_item'
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, related_name='order_item'
    )
    quantity = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return f"{self.item.fullname} in order {str(self.order.id)}"
