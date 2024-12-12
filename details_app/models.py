from django.db import models
from django.utils import timezone
import os
from django.dispatch import receiver
from django.db.models.signals import pre_delete

# Create your models here.
class DetailsModel(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    gmail = models.EmailField(max_length=50, unique=True)
    phone = models.BigIntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    images = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
 # Delete the associated image file when the profile is deleted
@receiver(pre_delete, sender=DetailsModel)
def delete_profile_image(sender, instance, **kwargs):
   
    if instance.images:
        # Use instance.images.path to get the absolute file path
        if os.path.isfile(instance.images.path):
            os.remove(instance.images.path)
    
