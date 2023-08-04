from django.shortcuts import render
from .forms import ImageUploadForm

# Create your views here.

def add_food_product(request):
    # form = ImageUploadForm()
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_desc = request.POST.get('product_desc')
        product_price = request.POST.get('product_price')
        product_quantity = request.POST.get('product_quantity')
        product_images = request.FILES.getlist('product_image')
        print("Product values are \n", product_name, product_desc, product_price, product_quantity, product_images)
    return render(request, 'add_food.html',)