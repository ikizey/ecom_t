from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Item(models.Model):

    fullname = models.CharField(max_length=500)
    description = models.TextField(max_length=1000, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='brand'
    )

    image = models.ImageField(
        default='item_images/default.jpg', upload_to='items_images'
    )

    def __str__(self):
        return self.fullname


class Banner(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner_images')

    def __str__(self):
        return self.description

