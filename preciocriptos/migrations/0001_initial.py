# Generated by Django 4.0 on 2022-01-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criptos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiker', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
    ]
