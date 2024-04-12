# Generated by Django 5.0.1 on 2024-02-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Contact2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=122)),
                ('email2', models.CharField(max_length=122)),
                ('phone2', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Res',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restaurant', models.CharField(max_length=122)),
            ],
        ),
    ]
