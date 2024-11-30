from django.contrib import admin
from .models import newtable
from .models import Employee,EmployeeNew,Department

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'department')  # Display specific fields in the admin list view
    search_fields = ('employee_name',)  # Add a search bar for the employee_name field

admin.site.register(Department)
admin.site.register(EmployeeNew)


# Register your models here.
@admin.register(newtable)
class registrationadmin(admin.ModelAdmin):
    list_display=('name','email')
# admin.py


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'salary', 'department')  # Show these fields in the list view


