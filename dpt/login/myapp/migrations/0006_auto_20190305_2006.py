# Generated by Django 2.1.5 on 2019-03-05 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190302_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_login',
            old_name='image',
            new_name='upload_logo',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='image',
            new_name='resume',
        ),
    ]