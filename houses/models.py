from django.db import models

# Create your models here.
class House(models.Model):
    """Model definition for house"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True, help_text="If house's owner allows pets or not.")
    
    def __str__(self):
        return self.name
    
