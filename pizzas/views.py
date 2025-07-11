from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):

    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by()
    context = {'pizzas':pizzas}
    return render(request,'pizzas/pizzas.html',context)




from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza, Comment
from .forms import CommentForm

def index(request):
    return render(request, 'pizzas/index.html') #homepage

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza_detail(request,pizza_id):
    pizza = get_object_or_404(Pizza,id=pizza_id)
    toppings = pizza.toppings.all()
    comments = pizza.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('pizzas:pizza_detail', pizza_id=pizza.id)
    else:
        form = CommentForm()
    
    context = {
        'pizza': pizza,
        'toppings': toppings,
        'comments': comments,
        'form': form
    }
    return render(request,'pizzas/pizza_detail.html',context)
