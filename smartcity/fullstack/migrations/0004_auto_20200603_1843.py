# Generated by Django 3.0.6 on 2020-06-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullstack', '0003_auto_20200603_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
