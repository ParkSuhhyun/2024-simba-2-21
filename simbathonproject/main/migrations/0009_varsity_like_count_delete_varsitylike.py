# Generated by Django 5.0.6 on 2024-06-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_varsity_like_count_varsitylike'),
    ]

    operations = [
        migrations.AddField(
            model_name='varsity',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Varsitylike',
        ),
    ]