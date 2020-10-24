# Generated by Django 2.2 on 2020-10-23 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201022_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='usertable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
    ]