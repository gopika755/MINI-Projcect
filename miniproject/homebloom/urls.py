from django.urls import path,include
from homebloom import views
urlpatterns = [
    path('',views.home,name='home'),
    path('shop',views.shop,name='shop'),
    path('category',views.category,name='category'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('cart',views.cart,name='cart'),
    path('login',views.login,name='login'),
    path("signup", views.signup, name="signup"),
    path('orders',views.orders,name='orders'),
    path('coupons',views.coupons,name='coupons'),
    path('notifications',views.notifications,name='notifications'),
]