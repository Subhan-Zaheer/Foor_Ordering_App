from django.db import models
import uuid

# Create your models here.

class BaseClass(models.Model):
    u_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    class Meta:
        abstract = True

class Product(BaseClass):
    product_name = models.CharField(max_length=60)
    product_quantity = models.IntegerField(null=True, blank=True, default=0)
    product_description = models.TextField()
    product_slug = models.SlugField(auto_created=True, null=True)
    product_price = models.IntegerField(default=0)
    product_measurement_unit = models.CharField(max_length=50,null=True, blank=True,
                                                 choices=(("KG", "KG"), ("ML", "ML"), ("L", "L"), ("None", None)))
    
    def __str__(self) -> str:
        return f"{self.product_name}"
    
class Product_Image(BaseClass):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    product_image = models.ImageField(upload_to='product/', default=None, null=True)

    def __str__(self) -> str:
        return f"Image of {self.product.product_name}"
    
