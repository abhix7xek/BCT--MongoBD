from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mobile, Cart


def index(request):
    return render(request, 'index.html')


def home(request):
    mobiles = Mobile.objects.all()
    return render(request, 'home.html', {'mobiles': mobiles})

def cart_view(request):
    return render(request, 'cart.html')  


def add_to_cart(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id)
    
    
    cart, created = Cart.objects.get_or_create(user=request.user)  
    
    cart.items.add(mobile) 
    return redirect('cart')  
