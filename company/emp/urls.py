from django.urls import path
from .api import *

urlpatterns = [
    # urls for Employee
    path('create', EmployeeCreateAPI.as_view()),
    path('alldata', EmployeeDataAPI.as_view()),
    path('onedata/<int:pk>', EmployeeOneDataAPI.as_view()),
    path('update/<int:pk>', EmployeeUpdateAPI.as_view()),
    path('upt/<int:pk>', EmployeeUpdatePartialAPI.as_view()),
    path('delete/<int:pk>', EmployeeDeleteAPI.as_view()),

]