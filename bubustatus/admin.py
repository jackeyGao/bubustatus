from django.contrib import admin
from bubustatus.models import Step, Label

# Register your models here.


class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')


class StepAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'insert', 'desc')

admin.site.register(Label, LabelAdmin)
admin.site.register(Step, StepAdmin)

