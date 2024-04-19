from django.db import models

class CarCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class CarList(models.Model):
    name = models.CharField(max_length=100, null= False)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(null= True)
    carcategories = models.ForeignKey(CarCategory, related_name="car_list", on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name

