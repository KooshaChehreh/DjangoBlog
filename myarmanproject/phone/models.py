from django.db import models

# Create your models here.

class Phone(models.Model):
    brand = models.CharField(max_length=50, blank=False, null=False)
    model = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.brand