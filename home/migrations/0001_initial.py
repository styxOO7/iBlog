# Generated by Django 3.2.5 on 2022-05-13 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('postId', models.IntegerField()),
                ('postTime', models.TextField(default='01:24AM')),
                ('postDate', models.TextField(default='May 14, 2022')),
                ('postImg', models.ImageField(blank=True, default='pic02.jpg', null=True, upload_to='')),
            ],
        ),
    ]
