# Generated by Django 3.0.7 on 2020-08-03 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial_app', '0003_auto_20200803_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
