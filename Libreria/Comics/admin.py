from django.contrib import admin
from Comics import models
# Register your models here.
admin.site.register(models.Comics)
admin.site.register(models.Tag)