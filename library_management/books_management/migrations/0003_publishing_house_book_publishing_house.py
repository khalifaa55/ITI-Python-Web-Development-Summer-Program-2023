# Generated by Django 4.2.4 on 2023-08-22 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_management', '0002_rename_book_isbn_book_isbn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='publishing_house',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books_management.publishing_house'),
        ),
    ]
