# Generated by Django 3.2.5 on 2022-05-18 20:00

from django.db import migrations, models
import djongo.storage


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20220519_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='postImg',
            field=models.ImageField(blank=True, default='pic02.jpg', null=True, storage=djongo.storage.GridFSStorage(base_url='/static/myfiles/', collection='myfiles'), upload_to='images'),
        ),
        migrations.AlterField(
            model_name='newpost',
            name='postTime',
            field=models.TextField(default='01:30AM'),
        ),
    ]
