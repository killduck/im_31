

from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def list_products(request):
    return render(request, 'list_products.html', {})


def add_category(request):
    return render(request, 'add_category.html', {})


