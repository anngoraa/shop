from django.urls import path
from .views import StoreView, AboutView, ShopView, ProductSingleView
urlpatterns = [
    path ('indexstore/', StoreView.as_view(), name='store_home'),
    path ('aboutstore/', AboutView.as_view(), name='about'),
    path('product/<int:product_id>/', ProductSingleView.as_view(), name='product_single'),
    path ('', ShopView.as_view(), name='shop'),

]





