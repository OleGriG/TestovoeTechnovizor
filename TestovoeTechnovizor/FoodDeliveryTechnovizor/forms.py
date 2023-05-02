from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['employee', 'delivery_datetime', 'dish']
        labels = {
            'employee': 'Имя сотрудника',
            'delivery_datetime': 'Дата',
            'dish': 'Блюдо'
        }
        widgets = {
            'employee': forms.RadioSelect,
            'delivery_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local', 'step': '60'}),
            'dish': forms.CheckboxSelectMultiple,
        }
