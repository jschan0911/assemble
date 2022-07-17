# Generated by Django 4.0.6 on 2022-07-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(max_length=13, null=True),
        ),
    ]