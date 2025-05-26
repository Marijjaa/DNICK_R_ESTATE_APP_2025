from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class RealEstate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    area = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='real_estates/', blank=True, null=True)
    characteristic = models.CharField(max_length=255, default="", null=True, blank=True)
    is_reserved = models.BooleanField(default=False)
    is_bought = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    linkedin_url = models.URLField(blank=True, null=True)
    number_of_sales = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.number_of_sales}"


class RealEstateAgent(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.real_estate.name} - {self.agent.name}"


class Characteristic(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class RealEstateCharacteristic(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.real_estate.name} - {self.characteristic.name}"
