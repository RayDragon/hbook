# Generated by Django 2.0 on 2018-02-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='creatorId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='details',
            field=models.TextField(null=True),
        ),
    ]