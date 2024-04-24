from django.contrib import admin

# Import the Donor and Contribution models
from .models import Donor, Contribution, Entity

# Register your models here.
# Donors needs to show id, name, address and needs_review
# and we need to search by name and address and needs review
@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'full_address', 'needs_review')
    search_fields = ('last_name', 'first_name', 'full_address')





admin.site.register(Contribution) # simple registration

# Register the Entity model but with some additional configuration allowing for filtering
# and searching by the entity_name field and classification.
@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity_name', 'office', 'year', 'report_name', 'state', 'classification')
    list_filter = ('classification',)
    search_fields = ('entity_name',)
