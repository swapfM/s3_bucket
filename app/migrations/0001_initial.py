# Generated by Django 3.2.6 on 2021-08-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('UserId', models.IntegerField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Pic', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
