from django.db import models
from django.contrib.auth import get_user_model


class Brand(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Item(models.Model):

    fullname = models.CharField(max_length=500)
    description = models.TextField(max_length=1000, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField(default=0)  # in kopeiki
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='brand'
    )

    image = models.ImageField(
        default='item_images/default.jpg', upload_to='items_images'
    )

    def __str__(self):
        return self.fullname

    @property
    def rub_price(self):
        return self.price / 100

    @rub_price.setter
    def set_rub_price(self, price_in_rub):
        self.price = price_in_rub * 100


class Banner(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner_images')

    def __str__(self):
        return self.description


class Order(models.Model):
    customer = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, related_name='order'
    )
    ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f"Order of {self.customer.username} on {self.ordered}"


class OrderItem(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True, related_name='order_item'
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, related_name='order_item'
    )
    quantity = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return f"{self.item.name} in order {str(self.order.id)}"

