from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Shopcard)
admin.site.register(Items)
admin.site.register(Product)
admin.site.register(Category)