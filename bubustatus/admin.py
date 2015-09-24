from django.contrib import admin
from bubustatus.models import Step, Label

# Register your models here.


class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'step_count', 'desc')


class StepAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_confirm', 'insert', 'confirm_time')
    list_filter = ('label', 'insert', 'confirm_time')
    search_fields = ('label', 'name', 'status')

admin.site.register(Label, LabelAdmin)
admin.site.register(Step, StepAdmin)

