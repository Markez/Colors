# Generated by Django 2.2 on 2019-07-27 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rangi', '0003_auto_20190727_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangi',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rangi.Company'),
        ),
    ]