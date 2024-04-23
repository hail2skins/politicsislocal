from django.contrib import admin
from .models import InvitationCode

@admin.register(InvitationCode)
class InvitationCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_used', 'created_at', 'expires_at')
    list_filter = ('is_used', 'created_at', 'expires_at')
    search_fields = ('code', 'user__username')
