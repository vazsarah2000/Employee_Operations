from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
# Create your models here.

class Emp_records(models.Model):
    GENDER_CHOICES = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'not specified'),
    )


    Name = models.CharField(max_length=200)
    PAN_number = models.CharField(max_length=10)
    Age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    Gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    Email = models.EmailField()
    City = models.CharField(max_length=100)


    def __str__(self):
        return self.Name


