from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class CustomUserAdmin(UserAdmin):
    # Add phoneNumber and profile_image fields to the list_display and fieldsets
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phoneNumber",
        "type",
        "profile_image_tag",  # To display the image in the list
        "is_staff",
    )

    fieldsets = UserAdmin.fieldsets + (
        (_("Additional Info"), {"fields": ("phoneNumber", "type", "image")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "phoneNumber",
                    "type",
                    "image",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    def profile_image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 45px; height: 45px;" />'.format(
                    obj.image.url
                )
            )
        return "-"

    profile_image_tag.short_description = "Profile Image"


admin.site.register(get_user_model(), CustomUserAdmin)
