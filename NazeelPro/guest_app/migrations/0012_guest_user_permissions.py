# Generated by Django 4.1.7 on 2023-06-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_app', '0011_guest_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='user_permissions',
            field=models.BooleanField(default=True),
        ),
    ]
