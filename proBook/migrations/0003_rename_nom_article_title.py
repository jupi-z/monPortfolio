# Generated by Django 4.2.3 on 2023-07-24 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proBook', '0002_rename_title_article_nom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='nom',
            new_name='title',
        ),
    ]
