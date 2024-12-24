from django.db import models

# Create your models here.


class owner (models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class labour(models.Model):
    la_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
     
     