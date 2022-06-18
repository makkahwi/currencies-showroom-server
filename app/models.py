from django.core.validators import MinValueValidator
from django.db import models


class Currency(models.Model):
    nation = models.CharField(max_length=256)
    currency = models.CharField(max_length=64)
    value = models.DecimalField(max_digits=20, decimal_places=3)
    unit = models.CharField(max_length=64)
    issueyear = models.DateField()
    circability = models.BooleanField(default=True)
    dissolved = models.BooleanField(default=False)
    count = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    collection = models.DateField()
    imgF = models.FileField()
    imgB = models.FileField()
    notes = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.currency}{self.value} of {self.nation}"
