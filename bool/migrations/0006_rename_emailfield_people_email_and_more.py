# Generated by Django 4.1.6 on 2023-02-03 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bool', '0005_people_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='EmailField',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='PasswordField',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='LoginField',
            new_name='username',
        ),
    ]