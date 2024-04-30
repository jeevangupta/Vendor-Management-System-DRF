from django.urls import path

from .views import (VendorReadCreateView, VendorFilterUpdateDeleteView,
                    PurchaseOrderReadCreateView, PurchaseOrderFilterUpdateDeleteView)

urlpatterns = [
    path('vendors/', VendorReadCreateView.as_view(), name='vendor-read-create'),
    path('vendors/<int:pk>/', VendorFilterUpdateDeleteView.as_view(), name='vendor-filter-update-delete'),

    path('purchase_orders/', PurchaseOrderReadCreateView.as_view(), name='order-read-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderFilterUpdateDeleteView.as_view(), name='order-filter-update-delete'),
]