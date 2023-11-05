from django.db import models
from django.core.validators import MaxValueValidator

# Модель "Clients"
class Clients(models.Model):
    ClientCode = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255)
    BankAccount = models.CharField(max_length=20)
    Phone = models.CharField(max_length=15)
    ContactPerson = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)

# Модель "Cars"
class Cars(models.Model):
    CarID = models.AutoField(primary_key=True)
    CAR_BRAND_CHOICES = [
        ('fiesta', 'Fiesta'),
        ('focus', 'Focus'),
        ('fusion', 'Fusion'),
        ('mondeo', 'Mondeo'),
    ]
    CarBrand = models.CharField(max_length=7, choices=CAR_BRAND_CHOICES)
    NewCarPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ClientCode = models.ForeignKey(Clients, on_delete=models.CASCADE)

# Модель "Repairs"
class Repairs(models.Model):
    RepairCode = models.AutoField(primary_key=True)
    RepairStartDate = models.DateField()
    CarCode = models.ForeignKey(Cars, on_delete=models.CASCADE)
    REPAIR_TYPE_CHOICES = [
        ('гарантійний', 'Гарантійний'),
        ('плановий', 'Плановий'),
        ('капітальний', 'Капітальний'),
    ]
    RepairType = models.CharField(max_length=15, choices=REPAIR_TYPE_CHOICES)
    HourlyRepairCost = models.DecimalField(max_digits=10, decimal_places=2)
    Discount = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    HoursRequired = models.PositiveSmallIntegerField()
