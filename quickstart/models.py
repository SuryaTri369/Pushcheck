from django.db import models
class newtable(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)

class Employee(models.Model):
    name = models.CharField(max_length=100)  # Employee's Name
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Salary with max 10 digits, 2 decimal places
    email = models.EmailField(unique=True)  # Employee's Email (must be unique)
    department = models.CharField(max_length=100)  # Department Name

    def __str__(self):
        return f"{self.name} - {self.department}"
    
# models.py
from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.department_name

class EmployeeNew(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name



        



   
# Create your models here.


