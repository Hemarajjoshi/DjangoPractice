# Generated by Django 5.0 on 2024-01-16 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateField()),
                ('moviename', models.CharField(max_length=100)),
                ('hero', models.CharField(max_length=100)),
                ('heroine', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]
