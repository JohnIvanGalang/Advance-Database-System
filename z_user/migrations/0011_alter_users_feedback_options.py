# Generated by Django 5.1.4 on 2025-02-27 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('z_user', '0010_users_feedback_coffee_alter_users_feedback_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users_feedback',
            options={'ordering': ['-commented_at'], 'verbose_name': 'Users Feedback', 'verbose_name_plural': 'Users Feedback'},
        ),
    ]
