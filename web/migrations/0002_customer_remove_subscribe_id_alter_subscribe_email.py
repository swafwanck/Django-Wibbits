# Generated by Django 4.1 on 2022-08-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='customer/')),
            ],
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='id',
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True),
        ),
    ]
