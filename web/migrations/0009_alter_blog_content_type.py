# Generated by Django 4.1 on 2022-09-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_testimonial_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content_type',
            field=models.TextField(choices=[('blog post', 'Blog post'), ('webinar', 'Webinar'), ('report', 'Report')]),
        ),
    ]
