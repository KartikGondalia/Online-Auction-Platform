# Generated by Django 2.1.7 on 2020-06-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]
