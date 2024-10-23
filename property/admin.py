from django.contrib import admin
from .models import PropertyFinance, PropertyMaintenanceInfo, PropertyManagement, PropertyTenantInfo


# Register your models here.


admin.site.register(PropertyManagement)
admin.site.register(PropertyTenantInfo)
admin.site.register(PropertyMaintenanceInfo)
admin.site.register(PropertyFinance)