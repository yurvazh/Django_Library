# Generated by Django 3.2.15 on 2022-10-01 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.author'),
        ),
    ]
