from django.contrib import admin
from .models import Birthday

# Register your models here.
@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    lit_display = ('name', 'birth_date', 'priority')
    list_filter = ('priority',)