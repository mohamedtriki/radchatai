# Generated by Django 4.1.7 on 2023-03-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_report_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='author',
            field=models.TextField(blank=True, default=''),
        ),
    ]
