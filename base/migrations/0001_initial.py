# Generated by Django 5.2 on 2025-05-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.IntegerField()),
                ('email_subject', models.CharField(max_length=100)),
                ('message_box', models.CharField(max_length=800)),
            ],
        ),
    ]
