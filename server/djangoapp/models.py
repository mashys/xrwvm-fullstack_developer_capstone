from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name  # Prints the make name, e.g., "Toyota"


class CarModel(models.Model):
    # Defining choices for the 'type' field
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon')
    ]
    
    # Many-to-One relationship with CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    
    # CharField with choices
    type = models.CharField(max_length=10, choices=CAR_TYPES, default=SUV)
    
    # IntegerField with min and max validators
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}" # Prints e.g., "Toyota Camry"