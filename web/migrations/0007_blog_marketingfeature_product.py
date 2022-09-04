# Generated by Django 4.1 on 2022-09-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Blog/images/')),
                ('title', models.CharField(max_length=255)),
                ('content_type', models.TextField(choices=[('blog', 'Blog'), ('webinar', 'Webinar'), ('report', 'Report')])),
            ],
        ),
        migrations.CreateModel(
            name='MarketingFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='makerting/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='product/images/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo', models.FileField(upload_to='product/logo/')),
            ],
        ),
    ]
