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
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('admin_product',views.admin_product,name='adminproduct'),
    path('admincategory',views.admincategory,name='admincategory'),
    path('adminorder',views.adminorder,name='adminorder'),
    path('admincoupon',views.admincoupon,name='admincoupon'),
    path('adminnotification',views.adminnotification,name='adminnotification'),
    path('adminuser',views.adminuser,name='adminuser'),
    path('checkout',views.checkout,name='checkout'),
]