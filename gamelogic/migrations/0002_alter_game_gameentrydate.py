# Generated by Django 4.1.5 on 2023-01-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelogic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameEntryDate',
            field=models.DateField(db_column='game_entry_date', default='2023-01-21', editable=False),
        ),
    ]
