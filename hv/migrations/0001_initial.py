# Generated by Django 4.0.6 on 2022-07-15 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alter_ego', models.CharField(max_length=100)),
                ('primary_ability', models.CharField(max_length=100)),
                ('secondary_ability', models.CharField(max_length=100)),
                ('catchphrase', models.CharField(max_length=100)),
            ],
        ),
    ]
