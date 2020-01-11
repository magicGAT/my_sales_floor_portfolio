# Generated by Django 2.0.2 on 2020-01-11 19:55

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
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=10000)),
                ('sources', models.CharField(max_length=500)),
            ],
        ),
    ]