from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Banner, Brand, Item, Order


class ManagerAdminMixin:
    """Gives permission to manager users"""

    def check_perm(self, user):
        if user.is_superuser or user.is_staff:
            return True
        return False

    def has_add_permission(self, request):
        return self.check_perm(request.user)

    def has_change_permission(self, request, obj=None):
        return self.check_perm(request.user)

    def has_delete_permission(self, request, obj=None):
        return self.check_perm(request.user)

    def has_module_permission(self, request):
        return self.check_perm(request.user)


@admin.register(Banner)
class BannerAdmin(ManagerAdminMixin, admin.ModelAdmin):
    search_fields = ['description']

    def banner_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}"')

    readonly_fields = ('banner_image',)


@admin.register(Brand)
class BrandAdmin(ManagerAdminMixin, admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Item)
class ItemAdmin(ManagerAdminMixin, admin.ModelAdmin):
    list_display = ('fullname', 'is_active', 'rub_price', 'brand')
    list_filter = ('is_active', 'brand')
    search_fields = ['fullname']

    def item_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="160" height="212"')

    readonly_fields = ('item_image',)


admin.site.register(Order)
