from django.urls import path
from . api import *

urlpatterns = [
    # urls for Staff
    
    path('create', StaffCreateAPI.as_view()),
    path('alldata', StaffAllDataAPI.as_view()),
    path('onedata/<int:pk>', StaffOneDataAPI.as_view()),
    path('update/<int:pk>', StaffUpdateAPI.as_view()),
    path('upt/<int:pk>', StaffUpdatePartialAPI.as_view()),
    path('delete/<int:pk>', StaffDeleteAPI.as_view()),
]