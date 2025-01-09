# Generated by Django 5.1.4 on 2025-01-09 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_user', '0006_alter_purchase_record_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('commented_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_user.user_account')),
            ],
        ),
    ]
