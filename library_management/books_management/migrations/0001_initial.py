# Generated by Django 4.2.4 on 2023-08-16 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_isbn', models.BigIntegerField()),
                ('book_name', models.CharField(max_length=200)),
                ('book_publish_date', models.DateField()),
            ],
        ),
    ]
