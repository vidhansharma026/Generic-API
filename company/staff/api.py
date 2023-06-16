from rest_framework import generics
from . models import *
from . serializers import StaffSerializer

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