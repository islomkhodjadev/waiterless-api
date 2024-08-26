from django.urls import path
from .views import OrderAPIView, OrderItemAPIView, OrderPlaceAPIView

urlpatterns = [
    path("orders/", OrderAPIView.as_view(), name="orders-list-create"),
    path("orders/<int:pk>/", OrderAPIView.as_view(), name="order-detail"),
    path("order-items/", OrderItemAPIView.as_view(), name="order-items-list-create"),
    path("order-items/<int:pk>/", OrderItemAPIView.as_view(), name="order-item-detail"),
    path("order-places/", OrderPlaceAPIView.as_view(), name="order-places-list-create"),
    path(
        "order-places/<int:pk>/", OrderPlaceAPIView.as_view(), name="order-place-detail"
    ),
]
