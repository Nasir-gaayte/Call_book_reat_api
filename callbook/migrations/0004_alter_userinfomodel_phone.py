# Generated by Django 4.2 on 2023-05-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callbook', '0003_alter_userinfomodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfomodel',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
