# Generated by Django 3.2.16 on 2024-01-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Released', 'Released')], default='Pending', max_length=50, null=True),
        ),
    ]
