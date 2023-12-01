# Generated by Django 4.2.5 on 2023-11-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_notification_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notification',
            name='filter_flag',
            field=models.CharField(choices=[('E', 'Every-Site-Visitor'), ('Q', 'All-Applicants'), ('P', 'Pending'), ('A', 'Accepted'), ('R', 'Rejected'), ('S', 'Specific-Applicant')], default='S', max_length=1),
        ),
    ]
