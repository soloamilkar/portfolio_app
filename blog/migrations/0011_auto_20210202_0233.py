# Generated by Django 3.1.5 on 2021-02-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210202_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/media/blog/default_blog.jpg', null=True, upload_to='blog/thumbnails/'),
        ),
    ]
