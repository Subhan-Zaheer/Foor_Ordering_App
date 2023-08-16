from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core import serializers


# Create your views here.

def add_food_product(request):
    # form = ImageUploadForm()

    if request.method == 'POST':
        
        product_images = request.FILES.getlist('product_image')
        
        product = Product.objects.create(
        product_name = request.POST.get('product_name'),
        product_description = request.POST.get('product_desc'),
        product_price = request.POST.get('product_price'),
        product_quantity = request.POST.get('product_quantity'),
        product_measurement_unit = request.POST.get('measurement_unit')
        )

    # Create the related Product_Image instances using the created Product instance
        for image in product_images:
            Product_Image.objects.create(product=product, product_image=image)
            # print("Product values are \n", product_name, product_desc, product_price, product_quantity, product_images,)
    return render(request, 'add_food.html',)

def update_product(request, name):

    product = Product.objects.get(product_name = name)
    images = product.product_images.all()
    data = {
        'product' : product,
        'images' : images,
    }
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.product_description = request.POST.get('product_desc')
        product.product_price = request.POST.get('product_price')
        product.product_quantity = request.POST.get('product_quantity')
        
        product_images = request.FILES.getlist('product_image') or images

        images.delete()
        for image in product_images:
            Product_Image.objects.create(product=product, product_image=image)

        product.save()
        product_list = [product]
        print(product_list)
        serialized_data = serializers.serialize('json', product_list)
        print(serialized_data)
        return redirect('/order-food')



    return render(request, 'update_product.html', data)

def food_display(request):
    
    products = Product_Image.objects.all()

    data = {
        'products' : products,
    }

    return render(request,'food_display.html', data)

def product_details(request, slug):
    product = Product.objects.get(product_slug = slug)
    images = product.product_images.all()
    for _ in images:
        print(f"Images of product are : {_}")

    data = {
        'product' : product, 
        'images' : images,
    }
    return render(request, 'product_details.html', data)

def add_to_cart(request, slug):
    product = Product.objects.get(product_slug = slug)
    print(product)
    if request.method == 'POST':

        quantity_input = int(request.POST.get('product_quantity_input'))
        print(quantity_input)
        print(product.product_quantity)
        print(type(quantity_input))
        if  quantity_input <= product.product_quantity:
            product.product_quantity -= quantity_input
            product.save()
        else:
            messages.warning(request, "Your quantity is more than stock.")

    return render(request, 'add_to_cart_page.html')