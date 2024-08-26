from django.db import models
from django.contrib.auth import get_user_model


class CafeModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="cafes/images", blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f"cafe: {self.name}"


class ProductCategoryModel(models.Model):
    cafe = models.ForeignKey(
        CafeModel, on_delete=models.CASCADE, related_name="category"
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="category/images", blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f"category: {self.name}"


class ProductModel(models.Model):
    category = models.ForeignKey(
        ProductCategoryModel, on_delete=models.CASCADE, related_name="product"
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product/images", blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return f"product: {self.name}"


class BranchModel(models.Model):
    cafe = models.ForeignKey(
        CafeModel, on_delete=models.CASCADE, related_name="branches"
    )
    location = models.URLField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="cafes/branches/")


class Places(models.Model):
    image = models.ImageField(upload_to="cafes/images/places/")
    number = models.PositiveIntegerField()
    branch = models.ForeignKey(
        BranchModel, on_delete=models.CASCADE, related_name="places"
    )
