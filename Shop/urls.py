from django.urls import path
from .views import ProductViewAdd,ProductView,ProductViewAll,Cartview

urlpatterns = [
    path ('product/add',ProductViewAdd.as_view()),
    path('product/<int:pk>',ProductView.as_view()),
    path("product/",ProductViewAll.as_view()),
    path("cart/",Cartview.as_view()),
]

