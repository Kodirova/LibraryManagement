# Generated by Django 3.1.3 on 2020-12-01 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201201_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='full_name',
            new_name='full_name_of_author',
        ),
    ]
