# Generated by Django 3.1.3 on 2020-12-04 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
    ]
