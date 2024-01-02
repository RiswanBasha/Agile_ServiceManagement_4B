# Generated by Django 3.2.16 on 2024-01-02 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/CustomerProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('by', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('agreement_name', models.CharField(max_length=100)),
                ('employee_name', models.CharField(max_length=100)),
                ('provider_name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('external_person', models.CharField(max_length=100)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('required_notes', models.CharField(max_length=255)),
                ('date_until', models.DateField(blank=True, null=True)),
                ('document_data', models.BinaryField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_information', models.CharField(max_length=1000, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('work_location', models.CharField(max_length=50, null=True)),
                ('contract_period', models.PositiveIntegerField(null=True)),
                ('domain', models.CharField(max_length=40)),
                ('role', models.CharField(max_length=40)),
                ('experience', models.CharField(choices=[('0-2', '0-2'), ('2-5', '2-5'), ('5-7', '5-7'), ('7+', '7+')], default='0-2', max_length=50)),
                ('technology', models.CharField(max_length=40)),
                ('further_skills', models.CharField(max_length=100, null=True)),
                ('upload_resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('onsite_days', models.PositiveIntegerField(null=True)),
                ('remote_days', models.PositiveIntegerField(null=True)),
                ('cost', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('In-Progress', 'In-Progress'), ('Repairing Done', 'Repairing Done'), ('Released', 'Released')], default='Pending', max_length=50, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.customer')),
                ('offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.offer')),
            ],
        ),
    ]
