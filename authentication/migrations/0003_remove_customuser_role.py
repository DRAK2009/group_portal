# Generated by Django 5.0.6 on 2024-10-02 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_customuser_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
    ]
