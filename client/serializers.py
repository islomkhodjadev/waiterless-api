from rest_framework import serializers
from .models import Order, OrderItem, OrderPlace
from cafe import models as cafeModels
from cafe import serializers as cafeSerializers
from user import serializers as userSerializers


class OrderSerializer(serializers.ModelSerializer):
    user = userSerializers.UserSerializer(read_only=True)
    order_place = cafeSerializers.PlacesSerializer(read_only=True)
    branch = cafeSerializers.BranchModelSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "time_created",
            "edited_time",
            "user",
            "complete",
            "order_place",
            "branch",
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    product = cafeSerializers.ProductModelSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "time_created",
            "edited_time",
            "count",
            "product",
            "order",
        ]


class OrderPlaceSerializer(serializers.ModelSerializer):
    order_place = cafeSerializers.PlacesSerializer(read_only=True)

    class Meta:
        model = OrderPlace
        fields = [
            "id",
            "time_created",
            "order_time",
            "order_place",
            "order_hours",
        ]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=OrderPlace.objects.all(), fields=["order_time", "order_place"]
            )
        ]
