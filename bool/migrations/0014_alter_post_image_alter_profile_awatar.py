# Generated by Django 4.1.6 on 2023-02-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bool', '0013_alter_post_image_alter_profile_awatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='awatar',
            field=models.ImageField(upload_to='awatars'),
        ),
    ]