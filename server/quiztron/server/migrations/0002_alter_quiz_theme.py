# Generated by Django 4.0.1 on 2022-01-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='theme',
            field=models.ManyToManyField(related_name='themes', through='server.ThemeOfQuiz', to='server.Theme'),
        ),
    ]