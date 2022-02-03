from django.contrib import admin
from Store.models import kontakt
from Store.models import Product
from Store.models import Cart
# Register your models here.
admin.site.register(kontakt)
admin.site.register(Product)
admin.site.register(Cart)