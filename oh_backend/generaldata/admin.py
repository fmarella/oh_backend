from django.contrib import admin

from generaldata.models import (Deliveryresulttype, Deliverytype, Dischargetype,
Diseasetype, Medicaldsrstockmovtype, Medicaldsrtype)


class DeliveryresulttypeAdmin(admin.ModelAdmin):
    list_display = ('drt_id_a', 'drt_desc')
    
class DeliverytypeAdmin(admin.ModelAdmin):
    list_display = ('dlt_id_a', 'dlt_desc')
    
class DischargetypeAdmin(admin.ModelAdmin):
    list_display = ('dist_id_a', 'dist_desc')
    
class DiseasetypeAdmin(admin.ModelAdmin):
    list_display = ('dcl_id_a', 'dcl_desc')
    
class MedicaldsrstockmovtypeAdmin(admin.ModelAdmin):
    list_display = ('mmvt_id_a', 'mmvt_desc', 'mmvt_type')
    
class MedicaldsrtypeAdmin(admin.ModelAdmin):
    list_display = ('mdsrt_id_a', 'mdsrt_desc')

admin.site.register(Deliveryresulttype, DeliveryresulttypeAdmin)
admin.site.register(Deliverytype, DeliverytypeAdmin)
admin.site.register(Dischargetype, DischargetypeAdmin)
admin.site.register(Diseasetype, DiseasetypeAdmin)
admin.site.register(Medicaldsrstockmovtype, MedicaldsrstockmovtypeAdmin)
admin.site.register(Medicaldsrtype, MedicaldsrtypeAdmin)

