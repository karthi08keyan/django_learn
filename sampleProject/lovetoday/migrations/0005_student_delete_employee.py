# Generated by Django 4.1.3 on 2022-11-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovetoday', '0004_alter_employee_empno_alter_employee_empsalary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_No', models.IntegerField()),
                ('student_Name', models.CharField(max_length=50)),
                ('student_Class', models.IntegerField()),
                ('student_Address', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
