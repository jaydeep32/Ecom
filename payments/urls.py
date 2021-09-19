from django.urls import path
from payments import views

urlpatterns = [
    path('', views.PaymentList.as_view(), name='payment'),
]
