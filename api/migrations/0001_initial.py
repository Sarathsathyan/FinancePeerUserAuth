# Generated by Django 4.0.4 on 2022-05-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jsonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(null=True)),
                ('title', models.TextField(null=True)),
                ('body', models.TextField(null=True)),
            ],
        ),
    ]