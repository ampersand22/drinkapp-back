# Generated by Django 4.1.1 on 2022-09-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('image', models.TextField()),
                ('ingredients', models.CharField(max_length=255)),
                ('comments', models.CharField(max_length=500)),
                ('likes', models.IntegerField()),
                ('locationDisplayName', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=200, null=True)),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=30, null=True)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=30, null=True)),
                ('tags', models.CharField(max_length=255)),
            ],
        ),
    ]