# Generated by Django 4.0.3 on 2022-05-11 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_alter_hirebook_due2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hirebook',
            name='due2',
            field=models.IntegerField(default=1998),
        ),
    ]
