# Generated by Django 3.0.6 on 2020-06-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fullstack', '0008_auto_20200604_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='document_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='fullstack.Document'),
        ),
    ]
