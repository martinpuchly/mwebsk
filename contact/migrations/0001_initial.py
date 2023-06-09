# Generated by Django 4.1.5 on 2023-02-01 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='predmet')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('message', models.TextField(verbose_name='správa')),
                ('read_over', models.BooleanField(default=False, verbose_name='prečítané')),
            ],
        ),
    ]
