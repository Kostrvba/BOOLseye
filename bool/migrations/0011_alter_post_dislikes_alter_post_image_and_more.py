# Generated by Django 4.1.6 on 2023-02-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bool', '0010_comments_created_post_created_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='awatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]