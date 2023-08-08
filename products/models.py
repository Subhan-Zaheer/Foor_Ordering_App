from django.db import models
import uuid
from django.db.models.signals import post_save, pre_delete, pre_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

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
    product_slug = models.SlugField(default=None)
    product_price = models.IntegerField(default=0)
    product_measurement_unit = models.CharField(max_length=50,null=True, blank=True,
                                                 choices=(("KG", "KG"), ("ML", "ML"), ("L", "L"), ("None", None)))
    
    def save(self, *args, **kwargs):
        # Generate the slug from the product name before saving
        if not self.product_slug:
            self.product_slug = slugify(self.product_name)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.product_name}"
    

def product_image_upload_path(instance, filename):
    # Construct the upload path with the product name and current timestamp
    return f'product/{instance.product.product_name}/{filename}'

class Product_Image(BaseClass):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    product_image = models.ImageField(upload_to=product_image_upload_path, default=None, null=True)
    
    # def __str__(self) -> str:
    #     return f"Image of {self.product.product_name}"
    

@receiver(pre_save, sender=Product)
def set_updated_at(sender, instance, update_fields, **kwargs):
    # Check if the 'updated_at' field is in the 'update_fields' list
    instance.updated_at = timezone.now() 

@receiver(pre_save, sender=Product_Image)
def set_updated_at(sender, instance, update_fields, **kwargs):
    # Check if the 'updated_at' field is in the 'update_fields' list
    instance.updated_at = timezone.now() 

@receiver(post_save, sender=Product)
def set_created_at(sender, instance, created, **kwargs):
    instance.created_at = timezone.now() if created and not instance.created_at else None

@receiver(post_save, sender=Product_Image)
def set_created_at(sender, instance, created, **kwargs):
    instance.created_at = timezone.now() if created and not instance.created_at else None