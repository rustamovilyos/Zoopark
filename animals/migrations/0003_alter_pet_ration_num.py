# Generated by Django 3.2.9 on 2021-11-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20211104_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='ration_num',
            field=models.IntegerField(max_length=4, null=True),
        ),
    ]
