# Generated by Django 4.1.3 on 2022-11-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_category_slug_alter_recipe_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, editable=False),
        ),
    ]
