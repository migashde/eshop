from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "sale", "image", "quantity", "category"]
    list_filter = ["name", "price", "sale", "image", "quantity", "category"]
    search_fields = ["name", "price", "sale", "image", "quantity", "category"]

admin.site.register(Product, ProductAdmin)
