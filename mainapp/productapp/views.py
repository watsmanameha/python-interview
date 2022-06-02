from django.shortcuts import render, HttpResponseRedirect
from .models import Product
from .forms import ProductForm

def index(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list
    }
    return render(request, 'productapp/goods_list.html', context)

def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()

    return render(request, 'productapp/form.html', {'form': form})