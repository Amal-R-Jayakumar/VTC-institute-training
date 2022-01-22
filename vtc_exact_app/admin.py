from django.contrib import admin
from vtc_exact_app.models import VtcModel, Batch

# Register your models here.
admin.site.register(VtcModel)
admin.site.register(Batch)