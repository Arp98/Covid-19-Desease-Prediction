# Generated by Django 3.1 on 2020-09-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=30)),
                ('pic', models.ImageField(upload_to='Team_Pics')),
            ],
        ),
    ]
