# Generated by Django 2.0.2 on 2018-03-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20180316_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
                ('post', models.ManyToManyField(to='post.Post')),
            ],
        ),
    ]
