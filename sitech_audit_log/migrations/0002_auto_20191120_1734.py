# Generated by Django 2.0.13 on 2019-11-20 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitech_audit_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaselogging',
            name='auditable_type',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Auditable Type'),
        ),
    ]
