# Generated by Django 2.1.7 on 2020-06-05 11:50

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200416_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadCast_Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'BroadCast Email to all Member',
                'verbose_name_plural': 'BroadCast Email',
            },
        ),
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
