# Generated by Django 4.1.3 on 2022-11-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovetoday', '0003_alter_employee_empno_alter_employee_empsalary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='empNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='empSalary',
            field=models.IntegerField(),
        ),
    ]
