from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class PropertyManagement(models.Model):
    property_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="static/img")
    address = models.CharField(max_length=200)
    property_type = models.CharField(max_length=50)
    number_of_units = models.CharField(max_length=10)
    year_built = models.TextField()
    square_footage = models.CharField(max_length=10)
    acquired_date = models.DateField()

    def __str__(self):
        return self.property_name

class PropertyFinance(models.Model):
    purchase_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    market_value = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    monthly_rent = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    operating_expenses = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    mortgage_details = models.TextField()
    property = models.ForeignKey(PropertyManagement, null=True, blank=True, on_delete=models.CASCADE)

    #def __str__(self):
        #return self.purchase_price

class PropertyTenantInfo(models.Model):
    name = models.CharField(max_length=128)
    lease_terms = models.CharField(max_length=50)
    rent_payment_status = models.CharField(max_length=10)
    property = models.ForeignKey(PropertyManagement, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PropertyMaintenanceInfo(models.Model):
    scheduled_maintenance = models.CharField(max_length=128)
    vendor = models.CharField(max_length=50)
    cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    property = models.ForeignKey(PropertyManagement, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.scheduled_maintenance


    