# Generated by Django 4.1.3 on 2022-11-27 11:26

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
                ('empNo', models.IntegerField(max_length=5)),
                ('empName', models.CharField(max_length=40)),
                ('empSalary', models.IntegerField(max_length=10)),
                ('empAddress', models.CharField(max_length=50)),
            ],
        ),
    ]
