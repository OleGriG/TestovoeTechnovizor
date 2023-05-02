from django.urls import path
from .views import home, order, history, bio

app_name = 'FoodDeliveryTechnovizor'
urlpatterns = [
    path('', home, name='home'),
    path('order/<int:order_id>/', order, name='order'),
    path('history/', history, name='history'),
    path('bio/', bio, name='bio')
]
