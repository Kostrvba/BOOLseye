# Generated by Django 4.1.6 on 2023-02-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bool', '0011_alter_post_dislikes_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
