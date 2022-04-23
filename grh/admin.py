from django.contrib import admin
from .models import Employe,Structure
# Register your models here.
@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ("lebel","str_mere","email")
    search_fields = ("lebel",)

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ("nom","prenom","email","structure")
    search_fields = ("nom","prenom")
    list_filter = ("structure",)