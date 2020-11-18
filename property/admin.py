from django.contrib import admin

from .models import Flat, Claim


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    raw_id_fields = ('likes',)
    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    list_display = (
        'address', 'price', 'new_building', 'construction_year', 'town',
        'owners_phonenumber', 'owner_pure_phone',
    )


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')
