from django.db import models
from django.contrib.auth import get_user_model
from cafe import models as cafeModels


# Create your models here.
class Order(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    edited_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="orders"
    )
    complete = models.BooleanField(default=False)
    order_place = models.ForeignKey(
        cafeModels.Places, on_delete=models.CASCADE, related_name="orders"
    )
    branch = models.ForeignKey(
        cafeModels.BranchModel, on_delete=models.CASCADE, related_name="orders"
    )


class OrderItem(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    edited_time = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField()
    product = models.ForeignKey(
        cafeModels.ProductModel, on_delete=models.CASCADE, related_name="orderitem"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="orderitems"
    )


class OrderPlace(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    order_time = models.DateTimeField()
    order_place = models.ForeignKey(
        cafeModels.Places, on_delete=models.CASCADE, related_name="orderPlaces"
    )
    order_hours = models.PositiveIntegerField()

    class Meta:
        unique_together = ("order_time", "order_place")
