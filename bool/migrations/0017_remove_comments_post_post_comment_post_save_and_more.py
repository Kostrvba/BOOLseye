# Generated by Django 4.1.6 on 2023-02-09 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bool', '0016_remove_post_likes_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bool.comments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='save',
            field=models.ManyToManyField(related_name='saved_post', to='bool.profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='comment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bool.comments'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Save',
        ),
    ]
