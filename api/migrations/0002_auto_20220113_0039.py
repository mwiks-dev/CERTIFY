# Generated by Django 3.2.9 on 2022-01-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='about',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='employer',
            name='reg_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='tel_number',
            field=models.IntegerField(null=True),
        ),
    ]
