from django.urls import path
from .views import PredictAPI
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', PredictAPI.as_view(), name='predict')
]
