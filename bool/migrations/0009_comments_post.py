# Generated by Django 4.1.6 on 2023-02-04 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bool', '0008_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bool.post'),
            preserve_default=False,
        ),
    ]