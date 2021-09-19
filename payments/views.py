from django.shortcuts import get_list_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from payments.models import Payment
from payments.serializers import PaymentSerializer


class PaymentList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = get_list_or_404(Payment, user=self.request.user)
        return queryset
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, ]
