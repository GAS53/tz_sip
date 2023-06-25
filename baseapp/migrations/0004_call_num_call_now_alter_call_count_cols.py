# Generated by Django 4.2.2 on 2023-06-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0003_alter_project_date_over_alter_project_date_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='num_call_now',
            field=models.SmallIntegerField(default=0, verbose_name='уже позвонили раз'),
        ),
        migrations.AlterField(
            model_name='call',
            name='count_cols',
            field=models.SmallIntegerField(default=1, verbose_name='сколько раз звонить, либо дозвон либо всего звонков'),
        ),
    ]
