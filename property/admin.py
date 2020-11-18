from django.contrib import admin

from .models import Flat, Claim, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('likes',)
    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    list_display = (
        'address', 'price', 'new_building', 'construction_year', 'town',
    )


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('owner',)
    list_display = ('owner', 'owners_phonenumber', 'owner_pure_phone',)
