from django.shortcuts import render, redirect
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def save(request):
    name = request.POST.get("name")
    Product.objects.create(name=name)
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, "update.html", {"product": product})

def update(request, id):
    name = request.POST.get("name")
    product = Product.objects.get(id=id)
    product.name = name
    product.save()
    return redirect(home)
