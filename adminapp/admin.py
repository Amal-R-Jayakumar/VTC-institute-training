from django.contrib import admin

from adminapp.models import District, Municipality, Corporation, Panchayath, VTCListExcel

# Register your models here.
admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Corporation)
admin.site.register(Panchayath)
admin.site.register(VTCListExcel)
# admin.site.register(TestQuestion)


