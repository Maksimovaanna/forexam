# Generated by Django 4.1.3 on 2023-01-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0005_mesta_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='predmet',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('nazvanie', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('audit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='uchet',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=50)),
                ('passw', models.CharField(max_length=50)),
                ('propusk', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='mesta',
        ),
        migrations.DeleteModel(
            name='spektakl',
        ),
    ]
