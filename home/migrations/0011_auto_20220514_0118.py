# Generated by Django 3.2.5 on 2022-05-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_newpost_posttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='postImg',
            field=models.ImageField(blank=True, default='pic02.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='newpost',
            name='postTime',
            field=models.TextField(default='01:18AM'),
        ),
    ]