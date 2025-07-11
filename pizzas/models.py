from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizza_name = ["Supreme","Veggie","Meat Lovers","Hawaiian","Cheese"]



class Topping(models.Model):
    pizza = ["Supreme","Veggie","Meat Lovers","Hawaiian","Cheese"]
    topping_name = ["Pepperoni","Sausage","Hamburger","Spinach","Olives","Pineapple","Canadian Bacon","3 Cheese Blend","Onion","Bacon"]