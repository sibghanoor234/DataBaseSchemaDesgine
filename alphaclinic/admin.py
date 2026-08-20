
from django.contrib import admin
from alphaclinic.models import Doctor, Patient, Appointment, Medicine,Labtests,Bill


# Register Doctor Model
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'email', 'phone', 'consultation_fees', 'created_at', 'updated_at')
    list_filter = ('specialization', 'consultation_fees')
    search_fields = ('name',)
admin.site.register(Doctor, DoctorAdmin)


# Register Patient Model
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'dob', 'email', 'address', 'blood_group', 'created_at', 'updated_at')
    list_filter = ('blood_group', 'gender')
    search_fields = ('name',)
admin.site.register(Patient, PatientAdmin)


# Register Appointment Model
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'remarks', 'status', 'created_at', 'updated_at')

admin.site.register(Appointment, AppointmentAdmin)

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id','medicine_name','price','stock','updated_at','created_at')
admin.site.register(Medicine,MedicineAdmin)

class LabtestAdmin(admin.ModelAdmin):
    list_display = ('id','test_name','price','discription','updated_at','created_at')
admin.site.register(Labtests , LabtestAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'doctor_fee', 'lab_total', 'medicine_total','tax','discount','payment_status','payment_method', 'created_at', 'updated_at')

admin.site.register(Bill, BillAdmin)
