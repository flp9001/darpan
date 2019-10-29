# Generated by Django 2.1.4 on 2019-06-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hds', '0004_auto_20190617_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='ravechart',
            name='undefined_centers',
            field=models.ManyToManyField(related_name='undefined', to='hds.Center'),
        ),
        migrations.AlterField(
            model_name='ravechart',
            name='defined_centers',
            field=models.ManyToManyField(related_name='defined', to='hds.Center'),
        ),
    ]