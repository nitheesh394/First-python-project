# Generated by Django 3.2.14 on 2022-08-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('img', models.ImageField(upload_to='pics')),
                ('det', models.TextField()),
            ],
        ),
    ]
