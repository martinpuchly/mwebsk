# Generated by Django 4.1.5 on 2023-02-01 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_tag_remove_post_tags_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='pages.tag', verbose_name='tagy'),
        ),
    ]
