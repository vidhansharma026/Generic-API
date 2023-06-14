from django.urls import path
from .api import *

urlpatterns = [
    # urls for Employee
    path('emp/create', EmployeeCreateAPI.as_view()),
    path('emp', EmployeeDataAPI.as_view()),
    path('emp/onedata/<int:pk>', EmployeeOneDataAPI.as_view()),
    path('emp/update/<int:pk>', EmployeeUpdateAPI.as_view()),
    path('emp/upt/<int:pk>', EmployeeUpdatePartialAPI.as_view()),
    path('emp/delete/<int:pk>', EmployeeDeleteAPI.as_view()),

    # urls for Staff
    path('staff/create', StaffCreateAPI.as_view()),
    path('staff', StaffAllDataAPI.as_view()),
    path('staff/onedata/<int:pk>', StaffOneDataAPI.as_view()),
    path('staff/update/<int:pk>', StaffUpdateAPI.as_view()),
    path('staff/upt/<int:pk>', StaffUpdatePartialAPI.as_view()),
    path('staff/delete/<int:pk>', StaffDeleteAPI.as_view()),
]