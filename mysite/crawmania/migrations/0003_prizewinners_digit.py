# Generated by Django 4.1 on 2022-08-31 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawmania', '0002_prizewinners'),
    ]

    operations = [
        migrations.AddField(
            model_name='prizewinners',
            name='digit',
            field=models.IntegerField(null=True),
        ),
    ]
