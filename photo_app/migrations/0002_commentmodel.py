# Generated by Django 2.2 on 2019-12-18 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20191218_0954'),
        ('photo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=200)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.UserModel')),
                ('parentpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo_app.Photomodel')),
            ],
        ),
    ]
