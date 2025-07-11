from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizzas = [
        ('supreme', 'Supreme'),
        ('veggie', 'Veggie'),
        ('meat_lovers', 'Meat Lovers'),
        ('hawaiian', 'Hawaiian'),
        ('cheese', 'Cheese'),
    ]
    
    pizza_name = models.CharField(max_length=200,choices=pizzas)

    def __str__(self):
        return self.pizza_name



class Topping(models.Model):
    pizza = [
        ('supreme', 'Supreme'),
        ('veggie', 'Veggie'),
        ('meat_lovers', 'Meat Lovers'),
        ('hawaiian', 'Hawaiian'),
        ('cheese', 'Cheese'),
    ]

    topping_name = [
        ('pepperoni', 'Pepperoni'),
        ('sausage', 'Sausage'),
        ('hamburger', 'Hamburger'),
        ('spinach', 'Spinach'),
        ('olives', 'Olives'),
        ('pineapple', 'Pineapple'),
        ('canadian_bacon', 'Canadian Bacon'),
        ('cheese_blend', '3 Cheese Blend'),
        ('onion', 'Onion'),
        ('bacon', 'Bacon'),
    ]

    pizza = models.CharField(max_length=200, choices=pizza)
    topping_name = models.CharField(max_length=200, choices=topping_name)

    def __str__(self):
        return f"{self.pizza} - {self.topping_name}"