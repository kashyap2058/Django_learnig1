# Generated by Django 5.0.1 on 2024-01-26 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_classroom_student_classroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=10)),
                ('roll_no', models.IntegerField()),
                ('bio', models.TextField(max_length=500)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='profile_pics')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
    ]
