# Generated by Django 3.2.11 on 2022-01-31 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
