from django.contrib import admin

# Import the Donor and Contribution models
from .models import Donor, Contribution, Entity

# Register your models here.
# This is the simplest way to register a model with the admin site
admin.site.register(Donor)
admin.site.register(Contribution)

# Register the Entity model but with some additional configuration allowing for filtering
# and searching by the entity_name field and classification.
@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity_name', 'office', 'year', 'report_name', 'state', 'classification')
    list_filter = ('classification',)
    search_fields = ('entity_name',)
