from rest_framework import serializers
from .models import BranchModel, CafeModel, Places, ProductCategoryModel, ProductModel


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["id", "name", "image", "description", "price"]


class ProductCategoryModelSerializer(serializers.ModelSerializer):
    products = ProductModelSerializer(many=True, read_only=True, source="product")

    class Meta:
        model = ProductCategoryModel
        fields = ["cafe", "id", "name", "image", "description", "products"]


class CafeModelSerializer(serializers.ModelSerializer):
    categories = ProductCategoryModelSerializer(
        many=True, read_only=True, source="category"
    )

    class Meta:
        model = CafeModel
        fields = ["user", "id", "name", "image", "description", "categories"]


class BranchModelSerializer(serializers.ModelSerializer):
    cafe = CafeModelSerializer(read_only=True)

    class Meta:
        model = BranchModel
        fields = ["id", "cafe", "location", "description", "image"]


class PlacesSerializer(serializers.ModelSerializer):
    branch = BranchModelSerializer(read_only=True)

    class Meta:
        model = Places
        fields = ["id", "image", "number", "branch"]
