# Generated by Django 4.2.3 on 2023-07-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proBook', '0003_rename_nom_article_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sujet', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
