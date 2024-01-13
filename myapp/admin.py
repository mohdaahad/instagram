from django.contrib import admin

# Register your models here.
from .models import UserLogin

admin.site.register(UserLogin)