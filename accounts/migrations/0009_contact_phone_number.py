# Generated by Django 4.0.1 on 2022-02-06 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
