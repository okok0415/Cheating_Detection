from django.contrib import admin
from . import models


@admin.register(models.Board)
class BoardAdmim(admin.ModelAdmin):

    list_display = (
        "title",
        "content",
        "user",
    )
