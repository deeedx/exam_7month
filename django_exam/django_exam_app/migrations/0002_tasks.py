# Generated by Django 4.2.7 on 2023-11-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_exam_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
