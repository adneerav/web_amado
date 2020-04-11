from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


# Create your views here.

def index(request):
    prod_list = Products.objects.all()
    return render(request, 'index.html', {'product_list': prod_list})


def home(request):
    return HttpResponse("Hello")


def product_detail(request):
    # prod_detail = Products.objects.
    return render(request, 'product-details.html')
