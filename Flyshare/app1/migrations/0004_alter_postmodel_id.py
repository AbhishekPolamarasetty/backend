# Generated by Django 3.2.15 on 2023-12-04 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_postmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
