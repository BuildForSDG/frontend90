# Generated by Django 3.0.6 on 2020-06-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullstack', '0004_auto_20200603_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]