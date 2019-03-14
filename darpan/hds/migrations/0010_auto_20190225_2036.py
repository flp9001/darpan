# Generated by Django 2.1.4 on 2019-02-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hds', '0009_channel_hexagram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Hexagram',
        ),
    ]
