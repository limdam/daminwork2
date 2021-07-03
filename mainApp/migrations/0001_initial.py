# Generated by Django 3.2.2 on 2021-07-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('latitude', models.FloatField(default=0.0)),
                ('longtitude', models.FloatField(default=0.0)),
            ],
        ),
    ]
