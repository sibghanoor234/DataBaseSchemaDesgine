
from django.contrib import admin
from ambulance.models import Ambulance,Emergency_call
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_number', 'driver_name', 'ambulance_type', 'ambulance_status', 'created_at', 'updated_at')
admin.site.register(Ambulance, AmbulanceAdmin)

class Emergency_callAdmin(admin.ModelAdmin):
    list_display = ('id', 'ambulance', 'patient_name', 'request_status', 'priority_status','request_time', 'created_at', 'updated_at')
admin.site.register(Emergency_call, Emergency_callAdmin)