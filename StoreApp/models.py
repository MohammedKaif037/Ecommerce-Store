from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    
class products(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='images/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,max_length=100)
    pid_for_home=models.IntegerField(default='0')

    def __str__(self) -> str:
        return self.title

