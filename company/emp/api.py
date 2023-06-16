from rest_framework import generics
from rest_framework.response import Response
from . models import *
from . serializers import *
# from django.contrib.auth.hashers import make_password
# from rest_framework_simplejwt.tokens import RefreshToken

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

# class RegistrationAPIView(generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def post(self,request):
#         data = request.POST.copy()
#         password = data.get('password')
#         data['password'] = make_password(password)
#         serializer = self.get_serializer(data = data)
#         serializer.is_valid(raise_exception = True)
#         emp = serializer.save()
#         refresh = RefreshToken.for_user(emp)
#         token = {
#             'refresh' : str(refresh),
#             'access' : str(refresh.access_token),
#         }
#         return Response(token)



