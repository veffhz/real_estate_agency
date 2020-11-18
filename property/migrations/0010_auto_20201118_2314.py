# Generated by Django 2.2.4 on 2020-11-18 19:09

from django.db import migrations


def create_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')  # noqa
    Owner = apps.get_model('property', 'Owner')  # noqa

    for flat in Flat.objects.all():
        owner = flat.owner
        owners_phonenumber = flat.owners_phonenumber
        owner_pure_phone = flat.owner_pure_phone
        owner, _ = Owner.objects.get_or_create(
            owner=owner,
            owners_phonenumber=owners_phonenumber,
            owner_pure_phone=owner_pure_phone,
        )

        flat.owners.set([owner])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(create_owners),
    ]
