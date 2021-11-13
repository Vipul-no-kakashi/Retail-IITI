from django.contrib import admin

# Register your models here.
from .models import Product, Cart, CartItem, Orders, Wishlist


admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Orders)
admin.site.register(Wishlist)