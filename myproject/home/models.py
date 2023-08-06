from django.db import models
from django.core.validators import RegexValidator

class PriceField(models.DecimalField):
    
        # Override the __init__ method to set some default arguments
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_digits", 10)
        kwargs.setdefault("decimal_places", 2)
        kwargs.setdefault("blank", True)
        kwargs.setdefault("null", True)

        super().__init__(*args, **kwargs)

    # Override the pre_save method to calculate the price before saving
    def pre_save(self, model_instance, add):
        """Calculate the price of a restaurant based on its reviews and other factors."""

        # Get the reviews from the model instance
        size = model_instance.size

        # Define some constants for calculation
        BASE_PRICE = 10.0
        SIZE_FACTOR = {"S": 1.0, "M": 1.2, "H": 1.4}

        # Calculate the price based on the reviews and other factors
        price = BASE_PRICE * SIZE_FACTOR[size]

        # Round the price to two decimal places
        price = round(price, 2)

        # Set the price attribute of the model instance
        setattr(model_instance, self.attname, price)
        # Return the price value
        return price

    

class Restaurant(models.Model):
    name= models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    PHONE_REGEX = r'^\+?1?\d{9,10}$'
    phone_validator = RegexValidator(regex=PHONE_REGEX, message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone = models.CharField(validators=[phone_validator], max_length=10, blank=True)
    
    CUISINE_CHOICES = [
        ('S',"low"),
        ('H',"high"),
        ('M',"mdedium")
    ]
    cuisine = models.CharField(max_length=1, choices=CUISINE_CHOICES)   
    
    rating = models.FloatField(max_length=50)
    REVIEW_CHOICES = [
        ('S',"low"),
        ('H',"high"),
        ('M',"mdedium")
    ]
    reviews = models.CharField(max_length=1,choices=REVIEW_CHOICES)
    price = PriceField(blank=True, null=True)
