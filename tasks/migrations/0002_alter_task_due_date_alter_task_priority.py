# Generated by Django 5.1.1 on 2024-09-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='M', max_length=1),
        ),
    ]
