# Generated by Django 4.2 on 2023-06-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_regno', models.TextField(unique=True)),
                ('employee_name', models.TextField()),
                ('employee_email', models.TextField()),
                ('employee_mobile', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
