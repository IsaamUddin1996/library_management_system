# Generated by Django 3.0.8 on 2020-12-09 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='library',
            old_name='writer',
            new_name='author',
        ),
    ]