from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmim(admin.ModelAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        ( 
            "Custom profile",
            {
                'fields': (
                    "supervisor",
                    "cellphoneNum",
            ),
        }),
    )