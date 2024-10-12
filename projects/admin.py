from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "name", "total_cost", "start_date", "complete_date"
    ]

admin.site.register(Project, ProjectAdmin)
