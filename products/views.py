from django.shortcuts import render, get_object_or_404, redirect
# from django.shortcuts import Http404

from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

def product_list_view(request):

    queryset = Product.objects.all()

    context = {
        'obj_list': queryset
    }

    return render(request, "products/product_list.html", context)

######################################################################

def product_create_view(request):

    # initial_data = {
    #     'summary': 'This is nice!',
    # }

    # obj = Product.objects.get(id=1)
    # form = ProductForm(request.POST or None, initial = initial_data, instance = obj)
    
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()
        # form = ProductForm(initial = initial_data)

    context = {
        'form': form
    }

    return render(request, "products/create.html", context)


def product_create_view2(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            form = RawProductForm()

    context = {
        'form': form
    }

    return render(request, "products/create.html", context)

######################################################################

def dynamic_lookup_view(request, id):

    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        'obj' : obj,
    }
    return render(request, "products/detail.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {
        'obj' : obj,
    }

    return render(request, "products/detail.html", context)

######################################################################

def product_delete_view(request, id):

    obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect('../../')

    context = {
        'obj' : obj,
    }
    return render(request, "products/delete.html", context)

######################################################################

def product_update_view(request, id):

    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect("../")

    context = {
        'form': form
    }

    return render(request, "products/create.html", context)