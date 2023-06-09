# Generated by Django 4.1.5 on 2023-02-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_quicknew_options_page_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titulok')),
                ('slug', models.SlugField(unique=True, verbose_name='URL link')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tagy',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='pages.tag', verbose_name='tagy'),
        ),
    ]
