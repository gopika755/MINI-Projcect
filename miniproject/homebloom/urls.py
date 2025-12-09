from django.urls import path,include
from homebloom import views
urlpatterns = [
    path('',views.home,name='home')
    
]