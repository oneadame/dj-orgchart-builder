# Generated by Django 2.0 on 2018-06-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makechart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='question_text',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='manager',
        ),
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ManyToManyField(related_name='_employee_manager_+', to='makechart.Employee'),
        ),
    ]
