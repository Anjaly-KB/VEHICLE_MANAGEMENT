# Generated by Django 4.1.1 on 2023-08-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('type', models.PositiveIntegerField()),
                ('model', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
