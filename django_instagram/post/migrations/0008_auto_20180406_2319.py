# Generated by Django 2.0.2 on 2018-04-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20180323_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reple',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='reple',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]