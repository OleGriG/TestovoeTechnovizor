from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Dish, Order
from .forms import OrderForm


def order(request, order_id):
    """
    View функция, которая рендерит страницу
    отчета о заказе, считает сумму заказа
    """
    order = get_object_or_404(Order, id=order_id)
    dishes = order.dish.all()
    total_sum = 0
    for dish in dishes:
        total_sum += dish.price
    print(dishes)
    context = {
        'order': order,
        'dishes': dishes,
        'total_sum': total_sum
    }
    return render(request, 'order.html', context)


def home(request):
    """
    View функция, которая рендерит главную
    страницу сайта и форму для оформления заказа
    """
    employees = Employee.objects.all()
    dishes = Dish.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.save()
            return redirect('FoodDeliveryTechnovizor:order', order_id=order.id)
    else:
        form = OrderForm()
    context = {'employees': employees, 'dishes': dishes, 'form': form}
    return render(request, 'home.html', context)


def history(request):
    """
    View функция для истории заказов
    """
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'history.html', context)


def bio(request):
    """
    View функция для старинцы обо мне
    """
    return render(request, 'bio.html')
