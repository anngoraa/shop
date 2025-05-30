from itertools import product

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from store.settings.info import INFO
from .models import Product


class StoreView(View):
 def get(self, request):
  contex = {}
  contex.update(INFO)
  return render(request, 'store/index.html', contex)

 def post(self, request):
  return JsonResponse(request.POST, json_dumps_params={'indent': 4})


class ProductSingleView(View):
 def get(self, request, product_id):
  product = Product.objects.get(id=product_id)
  context = {
   'product': product,
   'similar_products': Product.objects.exclude(id=product_id).order_by('?')[:4]
  }
  context.update(INFO)
  return render(request, 'store/product_single.html', context)

 def post(self, request):
  return JsonResponse(request.POST, json_dumps_params={'indent': 4})


class ShopView(View):
 def get(self, request):
  products_list = Product.objects.all()
  contex = {'page_obj': products_list}


  contex.update(INFO), contex
  return render(request, 'store/shop.html',contex)
 def post(self, request):
  return JsonResponse(request.POST, json_dumps_params={'indent': 4})



class AboutView(View):
 def get(self, request):
  contex = {}
  contex.update(INFO)
  return render(request, 'store/about.html', contex)
 def post(self, request):
  return JsonResponse(request.POST, json_dumps_params={'indent': 4})






# Create your views here.
