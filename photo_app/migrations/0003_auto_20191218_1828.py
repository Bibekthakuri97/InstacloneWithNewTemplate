# Generated by Django 2.2 on 2019-12-18 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0002_commentmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='parentpost',
            new_name='parent_post',
        ),
        migrations.RenameField(
            model_name='commentmodel',
            old_name='time_stamp',
            new_name='timestamp1',
        ),
    ]
