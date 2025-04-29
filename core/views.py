from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def save(request):
    name = request.POST.get("name")
    Product.objects.create(name=name)
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})