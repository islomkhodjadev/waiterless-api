from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView, status, Response
from rest_framework.permissions import IsAuthenticated

from .models import CafeModel, ProductCategoryModel, ProductModel
from .serializers import (
    CafeModelSerializer,
    ProductCategoryModelSerializer,
    ProductModelSerializer,
)


class CafeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cafes = CafeModel.objects.filter(user=request.user)

        return Response(
            data=CafeModelSerializer(cafes, many=True).data, status=status.HTTP_200_OK
        )

    def post(self, request):

        user = request.user
        data = request.data
        data["user"] = user.pk

        cafe = CafeModelSerializer(data=data)
        if cafe.is_valid(raise_exception=True):
            cafe = cafe.save()

            return Response(
                data=CafeModelSerializer(instance=cafe).data, status=status.HTTP_200_OK
            )

    def update(self, request, pk):
        data = request.data
        cafe = get_object_or_404(CafeModel, pk=pk, user=request.user)

        cafe = CafeModelSerializer(instance=cafe, data=data)
        if cafe.is_valid(raise_exception=True):
            cafe = cafe.save()

            return Response(
                data=CafeModelSerializer(instance=cafe).data, status=status.HTTP_200_OK
            )


class ProductCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, cafe_pk=None):
        # Fetch product categories related to a specific cafe
        cafe = get_object_or_404(CafeModel, pk=cafe_pk, user=request.user)
        categories = ProductCategoryModel.objects.filter(cafe=cafe)

        return Response(
            data=ProductCategoryModelSerializer(categories, many=True).data,
            status=status.HTTP_200_OK,
        )

    def post(self, request, cafe_pk=None):
        # Create a new product category for a cafe
        cafe = get_object_or_404(CafeModel, pk=cafe_pk, user=request.user)
        data = request.data
        data["cafe"] = cafe.pk  # Add cafe foreign key

        category = ProductCategoryModelSerializer(data=data)
        if category.is_valid(raise_exception=True):
            category = category.save()

            return Response(
                data=ProductCategoryModelSerializer(instance=category).data,
                status=status.HTTP_201_CREATED,
            )

    def patch(self, request, cafe_pk=None, category_pk=None):
        # Update a specific product category
        category = get_object_or_404(
            ProductCategoryModel,
            pk=category_pk,
            cafe__pk=cafe_pk,
            cafe__user=request.user,
        )
        data = request.data

        category = ProductCategoryModelSerializer(
            instance=category, data=data, partial=True
        )
        if category.is_valid(raise_exception=True):
            category = category.save()

            return Response(
                data=ProductCategoryModelSerializer(instance=category).data,
                status=status.HTTP_200_OK,
            )


class ProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category_pk=None):
        # Fetch products related to a specific category
        category = get_object_or_404(
            ProductCategoryModel, pk=category_pk, cafe__user=request.user
        )
        products = ProductModel.objects.filter(category=category)

        return Response(
            data=ProductModelSerializer(products, many=True).data,
            status=status.HTTP_200_OK,
        )

    def post(self, request, category_pk=None):
        # Create a new product under a specific category
        category = get_object_or_404(
            ProductCategoryModel, pk=category_pk, cafe__user=request.user
        )
        data = request.data
        data["category"] = category.pk  # Add category foreign key

        product = ProductModelSerializer(data=data)
        if product.is_valid(raise_exception=True):
            product = product.save()

            return Response(
                data=ProductModelSerializer(instance=product).data,
                status=status.HTTP_201_CREATED,
            )

    def patch(self, request, category_pk=None, product_pk=None):
        # Update a specific product
        product = get_object_or_404(
            ProductModel,
            pk=product_pk,
            category__pk=category_pk,
            category__cafe__user=request.user,
        )
        data = request.data

        product = ProductModelSerializer(instance=product, data=data, partial=True)
        if product.is_valid(raise_exception=True):
            product = product.save()

            return Response(
                data=ProductModelSerializer(instance=product).data,
                status=status.HTTP_200_OK,
            )
