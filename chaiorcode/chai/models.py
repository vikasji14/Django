from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Milk'),
        ('EG', 'Eggs'),
        ('CH', 'Cheese'),
        ('OT', 'Other'),
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')


    def __str__(self):
        return self.name 


# one to many relationship

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ratting = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
    

# many to many relationship
class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name
    
#  one to one relationship

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return self.name.chai
