import imp
from django.contrib import admin
from company.models import *

# Register your models here.


class ComapanyDetails(admin.ModelAdmin):
    list_display = ['company_name', 'company_size',
                    'company_created_by', 'company_created_at']
    ordering = ['company_size']


admin.site.register(Company, ComapanyDetails)
