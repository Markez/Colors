# Generated by Django 2.2 on 2019-05-12 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Rangi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_type', models.CharField(max_length=150)),
                ('rangi', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rangi.Company')),
            ],
        ),
    ]
