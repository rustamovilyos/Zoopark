# Generated by Django 3.2.9 on 2021-11-04 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_auto_20211104_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
