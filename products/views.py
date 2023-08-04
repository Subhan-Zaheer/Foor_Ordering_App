from django.shortcuts import render
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