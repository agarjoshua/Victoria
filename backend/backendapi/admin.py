from django.contrib import admin

from .models import Complaints
from .models import Stock
from .models import Order
# Register your models here.

admin.site.register(Complaints)
admin.site.register(Stock)
admin.site.register(Order)