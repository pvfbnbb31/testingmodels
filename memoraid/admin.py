from django.contrib import admin
from memoraid.models import Choice, Memoraid


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class MemoraidAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['memoraid_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('memoraid_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['memoraid_text']
	
admin.site.register(Memoraid, MemoraidAdmin)
