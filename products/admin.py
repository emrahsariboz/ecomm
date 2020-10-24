from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(ProductTable)
admin.site.register(usertable)
admin.site.register(order)


