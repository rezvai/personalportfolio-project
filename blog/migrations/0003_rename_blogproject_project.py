# Generated by Django 4.1.7 on 2023-04-01 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogproject_delete_blogs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogProject',
            new_name='Project',
        ),
    ]
