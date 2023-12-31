# Generated by Django 4.0.4 on 2022-05-09 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_submission_is_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='allotted_ta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ta', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor', to=settings.AUTH_USER_MODEL),
        ),
    ]
