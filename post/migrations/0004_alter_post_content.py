# Generated by Django 3.2.5 on 2021-07-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_created_ad_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Контент'),
        ),
    ]