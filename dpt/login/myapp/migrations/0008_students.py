# Generated by Django 2.1.5 on 2019-04-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20190312_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student_number', models.IntegerField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(blank=True, max_length=20, null=True)),
                ('l_name', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=144, null=True)),
                ('county', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('gpa', models.IntegerField(blank=True, null=True)),
                ('passwords', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
