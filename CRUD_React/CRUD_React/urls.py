from django.contrib import admin
from django.urls import path, include           
from rest_framework import routers              
from Crud import views                          
        
router = routers.DefaultRouter()                
router.register(r'posts', views.PostView, 'Crud')
        
urlpatterns = [
    path('admin/', admin.site.urls),           
    path('', include(router.urls))          
]