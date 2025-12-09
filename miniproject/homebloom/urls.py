from django.urls import path,include
from homebloom import views
urlpatterns = [
    path('',views.home,name='home'),
    path('shop',views.shop,name='shop'),
    path('category',views.category,name='category'),
]