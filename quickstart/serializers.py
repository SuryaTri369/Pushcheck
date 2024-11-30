from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import newtable, Employee
from quickstart import models


# users/serializers.py

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'salary', 'email', 'department']


class UserSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=70)
    email= serializers.EmailField(max_length=70)

    def create(self, validated_data):
        return newtable.objects.create(**validated_data)  
    def update(self, employee, validated_data):
        newemployee=newtable(**validated_data)
        newemployee.id=employee.id
        newemployee.save()
        return newemployee
        #class Meta:
        #model = User
       # fields = ['url', 'username', 'email', 'groups']
# serializers.py
from rest_framework import serializers
from .models import EmployeeNew, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_id', 'department_name']
        read_only_fields = ['department_id']

class NewEmployeeSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source='department')  # Nested serializer for department

    class Meta:
        model = EmployeeNew
        fields = ['employee_id', 'employee_name', 'department_id']




#class GroupSerializer(serializers.HyperlinkedModelSerializer):
   # class Meta:
       # model = Group
       # fields = ['url', 'name']
