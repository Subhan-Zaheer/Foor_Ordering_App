from django.shortcuts import render, redirect
from .models import *


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
        return redirect('/order-food')



    return render(request, 'update_product.html', data)

def food_display(request):
    
    return render(request,'food_display.html')