# Generated by Django 2.0.4 on 2018-04-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0005_auto_20180409_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='uuid',
            field=models.CharField(default='530632c8', max_length=200),
        ),
    ]
