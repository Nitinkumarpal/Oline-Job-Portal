# Generated by Django 2.1.5 on 2019-02-21 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=50)),
                ('years_of_stablish', models.DateTimeField()),
                ('location', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=12)),
            ],
        ),
    ]
