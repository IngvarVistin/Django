from django.urls import path
from basket.wiews import basket_add

app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>', basket_add, name='basket_add'),
]