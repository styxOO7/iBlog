# Generated by Django 3.2.5 on 2022-05-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_newpost_posttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='postTime',
            field=models.TextField(default='01:52AM'),
        ),
    ]
