from django.contrib import admin
from . import models

# Register your models here.


# make model to form
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
