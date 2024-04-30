from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import (Vendor)
from .serializers import (VendorSerializer)


class VendorReadCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorFilterUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
