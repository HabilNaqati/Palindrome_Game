# Generated by Django 4.1.5 on 2023-01-21 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userEntryDate',
            field=models.DateField(blank=True, db_column='user_entry_date', default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userModifiedDate',
            field=models.DateField(blank=True, db_column='user_modified_date', default=django.utils.timezone.now, null=True),
        ),
    ]
