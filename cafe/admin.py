from django.utils.html import format_html
from django.contrib import admin
from .models import CafeModel, ProductCategoryModel, ProductModel


# Utility function for image preview in admin panel
def get_image_preview(obj):
    if obj.image:
        return format_html(
            '<img src="{}" style="width: 50px; height:50px;" />', obj.image.url
        )
    return "No Image"


# Inline for ProductModel with image previews
class ProductModelInline(admin.TabularInline):
    model = ProductModel
    extra = 1
    fields = ["name", "price", "quantity", "image", "image_preview", "description"]
    readonly_fields = ["image_preview"]

    # To show the image preview within inline
    def image_preview(self, obj):
        return get_image_preview(obj)

    image_preview.short_description = "Preview"


# Inline for ProductCategoryModel with image previews
class ProductCategoryModelInline(admin.TabularInline):
    model = ProductCategoryModel
    extra = 1
    fields = ["name", "image", "image_preview", "description"]
    readonly_fields = ["image_preview"]

    # To show the image preview within inline
    def image_preview(self, obj):
        return get_image_preview(obj)

    image_preview.short_description = "Preview"


# Admin for CafeModel with inline categories and image preview
@admin.register(CafeModel)
class CafeAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "image_preview", "description")
    search_fields = ["name", "user"]
    inlines = [ProductCategoryModelInline]
    list_filter = ["name", "user"]
    readonly_fields = ["image_preview"]

    # To show the image preview
    def image_preview(self, obj):
        return get_image_preview(obj)

    image_preview.short_description = "Image"

    # Add extra actions for easy creation or deletion
    actions = ["delete_selected"]

    # To delete selected items
    def delete_selected(self, request, queryset):
        queryset.delete()
        self.message_user(request, "Selected cafes were deleted successfully.")


# Admin for ProductCategoryModel with inline products and image preview
@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "cafe", "image_preview", "description")
    search_fields = ["name", "cafe__name"]
    list_filter = ["cafe"]
    inlines = [ProductModelInline]
    readonly_fields = ["image_preview"]

    # To show the image preview
    def image_preview(self, obj):
        return get_image_preview(obj)

    image_preview.short_description = "Image"

    # Custom actions
    actions = ["delete_selected"]


# Admin for ProductModel with image preview and filters
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "image_preview",
        "description",
        "category",
    )
    search_fields = ["name", "category__name"]
    list_filter = ["category", "price"]
    readonly_fields = ["image_preview"]

    # To show the image preview
    def image_preview(self, obj):
        return get_image_preview(obj)

    image_preview.short_description = "Image"

    # Custom actions
    actions = ["delete_selected"]

    # Override delete_selected method
    def delete_selected(self, request, queryset):
        queryset.delete()
        self.message_user(request, "Selected products were deleted successfully.")
