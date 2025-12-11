from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
# Create your views here.
def shop(request):
    return render(request,'shop.html')
def category(request):
    return render(request,'category.html')
def wishlist(request):
    return render(request,'wishlist.html')
def cart(request):
    return render(request,'cart.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request, "signup.html")
def orders(request):
    return render(request,'orders.html')
def coupons(request):
    return render(request,'coupons.html')
def notifications(request):
    return render(request,'notifications.html')