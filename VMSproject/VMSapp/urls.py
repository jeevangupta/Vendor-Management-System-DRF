from django.urls import path

from .views import (VendorReadCreate, VendorFilterUpdateDelete,
                    PurchaseOrderReadCreate, PurchaseOrderFilterUpdateDelete,
                    Performance, AcknowledgeOrder)

urlpatterns = [
    path('vendors/', VendorReadCreate.as_view(), name='vendor-read-create'),
    path('vendors/<int:pk>/', VendorFilterUpdateDelete.as_view(), name='vendor-filter-update-delete'),

    path('purchase_orders/', PurchaseOrderReadCreate.as_view(), name='order-read-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderFilterUpdateDelete.as_view(), name='order-filter-update-delete'),

    path('vendors/<int:pk>/performance/', Performance.as_view(), name='performance'),
    path('purchase_orders/<int:pk>/acknowledge/', AcknowledgeOrder.as_view(), name='acknowledge-order'),

]