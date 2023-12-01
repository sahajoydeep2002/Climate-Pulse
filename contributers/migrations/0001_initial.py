# Generated by Django 4.2.2 on 2023-08-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contributersDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.TextField(max_length=50)),
                ('c_image', models.ImageField(upload_to='contributersImage')),
                ('c_bio', models.TextField(max_length=200)),
            ],
        ),
    ]