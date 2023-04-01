# Generated by Django 4.1.7 on 2023-04-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_blogproject_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]