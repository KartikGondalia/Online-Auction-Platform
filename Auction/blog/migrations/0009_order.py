# Generated by Django 2.1.7 on 2020-06-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200416_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('payment_status', models.CharField(choices=[('incomplete', 'incomplete'), ('complete', 'complete')], default='incomplete', max_length=50)),
            ],
        ),
    ]
