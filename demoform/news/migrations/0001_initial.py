# Generated by Django 2.2 on 2021-03-10 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 3, 10, 20, 48, 21, 814268))),
            ],
        ),
    ]
