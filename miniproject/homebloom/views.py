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