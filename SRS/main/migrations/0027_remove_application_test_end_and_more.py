# Generated by Django 4.2.5 on 2023-11-30 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_applicantresponse_ques'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='test_end',
        ),
        migrations.RemoveField(
            model_name='application',
            name='test_start',
        ),
    ]