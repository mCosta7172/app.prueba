# Generated by Django 2.2.6 on 2019-11-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0002_auto_20191119_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jgp', upload_to='profile_pics'),
        ),
    ]
