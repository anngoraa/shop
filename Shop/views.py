from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Product, Cart
from django.shortcuts import get_object_or_404
from .models import User
# Create your views here.
class ProductViewAdd(View):
 def get(self, request):
     params = request.GET
     input_type = params.get('type')
     valid_types = dict(Product.type_choises).keys()
     if input_type in valid_types:
         final_type = input_type
     else:
         final_type = 'Not Stated'
     product = Product(name=params['name'], type=final_type)
     try:
         product.save()
     except Exception as e:
         return HttpResponse(f"Product was created error boy {e}-----{params['name']}")
     return HttpResponse(f"Product '{params['name']}' with type '{final_type}' created hhhrrrmimimi")

class ProductView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product,pk=pk)
        return HttpResponse(f"Product Type  {product.get_type_display()},Product name {product}")


# class ProductViewAll(View):
#     def get(self,request):
#         product =Product.objects.all()
#         res = ''
#         for i in product:
#             res += str(i)
#         return HttpResponse(f"All {res}")



class ProductViewAll(View):
    def get(self, request):
        product = Product.objects.all()
        if 'type' in request.GET:
            product = product.filter(type=request.GET['type'])
        print(product)
        return HttpResponse(product)

class Cartview(View):
    def get(self, request):
        email = request.GET['email']
        cart = Cart.objects.filter(user_id__email=email).order_by('-create_at')
        print(cart)
        return HttpResponse(cart)
        # user = request.GET['user']
        # cart = Cart.objects.filter(pk=user)





