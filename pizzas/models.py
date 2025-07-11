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
    
    pizza_name = models.CharField(max_length=200,choices=pizzas,default='cheese')

    def __str__(self):
        return self.pizza_name



class Topping(models.Model):

    toppings = [
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

    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200,choices=toppings,default='cheese_blend')

    def __str__(self):
        return f"{self.pizza} - {self.topping_name}"
    

class Comment(models.Model):

    product = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.text[:20]}..."