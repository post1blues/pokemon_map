# Generated by Django 3.1.13 on 2021-09-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20210912_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]