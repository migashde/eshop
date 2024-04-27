from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product


def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, "home.html", context)

def category(request, cat_id):
    context = {
        'products': Product.objects.filter(category_id=cat_id)
    }
    return render(request, "home.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, "Username or Password does not match...")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('login')
