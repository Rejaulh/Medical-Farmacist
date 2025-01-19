from django.contrib import admin
from .models import Medicine

# Register your models here.
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost_price', 'stock', 'expiry_date')  # Columns to display in the list view
    list_filter = ('expiry_date',)  # Filters for the right sidebar
    search_fields = ('name', 'description')  # Searchable fields
    ordering = ('-expiry_date',)  # Default ordering
    fields = ('name', 'description', 'cost_price', 'stock', 'expiry_date')  # Fields to display in the detail view