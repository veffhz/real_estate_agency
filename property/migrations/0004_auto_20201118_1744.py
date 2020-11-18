# Generated by Django 2.2.4 on 2020-11-18 14:44

from django.db import migrations


def set_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat') # noqa
    for flat in Flat.objects.all():
        flat.new_building = True if flat.construction_year >= 2015 else False
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(set_new_building_field),
    ]