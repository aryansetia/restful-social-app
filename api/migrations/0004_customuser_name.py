# Generated by Django 5.0 on 2024-01-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='name'),
            preserve_default=False,
        ),
    ]