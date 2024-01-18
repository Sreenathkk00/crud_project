from django.db import models
from django.utils import timezone

# Create your models here.

class DetailsModel(models.Model):
    """class Meta:
        db_table= 'detailsmodel' # forgot to define before migration
"""
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

    
