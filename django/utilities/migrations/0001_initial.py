# Generated by Django 3.2.18 on 2023-03-17 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', upload_to='images/%Y/%m/%d/', verbose_name='image')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Alternative text')),
            ],
        ),
    ]
