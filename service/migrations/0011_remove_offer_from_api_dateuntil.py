# Generated by Django 3.2.16 on 2024-01-15 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_alter_offer_from_api_dateuntil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer_from_api',
            name='dateuntil',
        ),
    ]