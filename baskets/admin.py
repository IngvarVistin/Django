from django.contrib import admin

from baskets.model import Basket

class BasketAdmin(admin.TabularInLine):
    model = Basket
    fields = ('products', 'quantity', 'created_timestamp')
    readonli_fields = ('created_timestamp',)
