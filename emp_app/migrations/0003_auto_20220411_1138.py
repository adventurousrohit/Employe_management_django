# Generated by Django 3.0.14 on 2022-04-11 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_employee_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
