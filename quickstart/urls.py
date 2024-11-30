from django.urls import path
from . import views
from .views import new_employee_list, new_employee_detail,department_list,department_detail


urlpatterns = [
    path('employees/', views.employee_list, name='employee-list'),  # For GET and POST
    path('employees/<int:pk>/', views.employee_detail, name='employee-detail'),  # For GET, PUT, DELETE
    path('employeesnew/', new_employee_list, name='employee_list'),
    path('employeesnew/<int:pk>/', new_employee_detail, name='employee_detail'),
    path('departments/', department_list, name='department_list'),
    path('departments/<int:pk>/', department_detail, name='department_detail'),

]
# urls.py
