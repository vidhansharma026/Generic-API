from rest_framework import generics
from . models import *
from . serializers import *

# class for employee api

class EmployeeCreateAPI(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDataAPI(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeOneDataAPI(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateAPI(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdatePartialAPI(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDeleteAPI(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# class for employee api

class StaffCreateAPI(generics.CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffAllDataAPI(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffOneDataAPI(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffUpdateAPI(generics.UpdateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffUpdatePartialAPI(generics.RetrieveUpdateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffDeleteAPI(generics.DestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

