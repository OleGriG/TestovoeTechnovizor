from django.db import models


class Employee(models.Model):
    """ Модель сотрудника """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    """ Модель блюда """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    """ Модель заказа """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dish = models.ManyToManyField(Dish, related_name='orders')
    delivery_datetime = models.DateTimeField()

    def __str__(self):     
        dishes = ", ".join([str(d) for d in self.dish.all()])
        return f'{self.employee} - {dishes} - {self.delivery_datetime}'
