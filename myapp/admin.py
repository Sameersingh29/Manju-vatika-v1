# admin.py

from django.contrib import admin
from .models import Enquiry, Event

class EventInline(admin.TabularInline):
    model = Event
    extra = 1

class EnquiryAdmin(admin.ModelAdmin):
    inlines = [EventInline]
    list_display = ('first_name', 'last_name', 'email', 'phone', 'event_date', 'guest_count', 'event_type', 'status')
    list_filter = ('event_type', 'status')
    search_fields = ('first_name', 'last_name', 'email', 'phone')

admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Event)
