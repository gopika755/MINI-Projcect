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
def adminpanel(request):
    return render(request,'adminpanel.html')
def admin_product(request):
    return render(request,'admin_product.html')
def admincategory(request):
    return render(request,'admincategory.html')
def adminorder(request):
    return render(request,'adminorder.html')
def admincoupon(request):
    return render(request,'admincoupon.html')
def adminnotification(request):
    return render(request,'adminnotification.html')
def adminuser(request):
    return render(request,'adminuser.html')
def checkout(request):
    return render(request,'checkout.html')