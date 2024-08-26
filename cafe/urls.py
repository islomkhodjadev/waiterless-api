from django.urls import path
from .views import CafeView, ProductCategoryView, ProductView

urlpatterns = [
    path("cafes/", CafeView.as_view(), name="cafe-list-create"),
    path("cafes/<int:pk>/", CafeView.as_view(), name="cafe-update"),
    path(
        "cafes/<int:cafe_pk>/categories/",
        ProductCategoryView.as_view(),
        name="category-list-create",
    ),
    path(
        "cafes/<int:cafe_pk>/categories/<int:category_pk>/",
        ProductCategoryView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:category_pk>/products/",
        ProductView.as_view(),
        name="product-list-create",
    ),
    path(
        "categories/<int:category_pk>/products/<int:product_pk>/",
        ProductView.as_view(),
        name="product-update",
    ),
]
