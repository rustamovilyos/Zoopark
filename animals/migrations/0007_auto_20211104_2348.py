# Generated by Django 3.2.9 on 2021-11-04 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0006_auto_20211104_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='caretaker',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('baby', 'baby')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='veterinarian',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('baby', 'baby')], max_length=6, null=True),
        ),
    ]
