# Generated by Django 2.2.6 on 2019-10-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit_cup', '0003_auto_20191023_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]