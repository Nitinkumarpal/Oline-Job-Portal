# Generated by Django 2.1.5 on 2019-04-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_delete_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseaker_login',
            name='image',
            field=models.ImageField(blank=True, upload_to='company/%Y/%m/%d'),
        ),
    ]
