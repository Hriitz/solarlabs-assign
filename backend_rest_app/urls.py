from django.urls import path
from . import views

urlpatterns = [
    path('country_info/<country_name>', views.country_info)
]
