# Generated by Django 4.1.5 on 2023-02-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_commentmodel_from_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('family', models.CharField(default='barbar', max_length=200)),
                ('is_ok', models.BooleanField()),
            ],
        ),
    ]
