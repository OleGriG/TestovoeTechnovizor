from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('FoodDeliveryTechnovizor.urls',
                     namespace='FoodDeliveryTechnovizor')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]
