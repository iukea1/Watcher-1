# Generated by Django 3.0.5 on 2020-04-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_monitoring', '0009_auto_20200424_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='monitored',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]