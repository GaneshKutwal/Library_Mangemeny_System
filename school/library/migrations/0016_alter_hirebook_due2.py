# Generated by Django 4.0.3 on 2022-05-11 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_alter_hirebook_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hirebook',
            name='due2',
            field=models.IntegerField(default=0),
        ),
    ]
