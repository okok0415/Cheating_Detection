from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.Book)


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": ("supervisor", "nickname", "student_number", "birth"),
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("supervisor",)

    list_display = (
        "username",
        "nickname",
        "email",
        "student_number",
        "birth",
        "supervisor",
    )
