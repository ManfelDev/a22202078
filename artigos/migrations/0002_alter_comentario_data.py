# Generated by Django 5.1.3 on 2025-03-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artigos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comentario",
            name="data",
            field=models.DateField(),
        ),
    ]
