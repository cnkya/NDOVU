# Generated by Django 5.1.1 on 2024-10-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AlterField(
            model_name='project',
            name='complete_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
