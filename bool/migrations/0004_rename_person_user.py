# Generated by Django 4.1.6 on 2023-02-03 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bool', '0003_rename_user_person'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='User',
        ),
    ]