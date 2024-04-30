from django.urls import path

from .views import (VendorReadCreateView, VendorFilterUpdateDeleteView)

urlpatterns = [
    path('vendors/', VendorReadCreateView.as_view(), name='vendor-read-create'),
    path('vendors/<int:pk>/', VendorFilterUpdateDeleteView.as_view(), name='vendor-filter-update-delete'),
]