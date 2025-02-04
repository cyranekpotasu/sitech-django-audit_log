# Generated by Django 2.0.13 on 2019-11-06 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import sitech_middlewares.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseLogging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditable_id', models.PositiveIntegerField(verbose_name='Auditable Id')),
                ('auditable_type', models.CharField(max_length=255, verbose_name='Auditable Type')),
                ('operation', models.CharField(max_length=255, verbose_name='Operation')),
                ('values', jsonfield.fields.JSONField(verbose_name='Values')),
                ('creator_ip', models.GenericIPAddressField(null=True)),
                ('creator_agent', models.CharField(max_length=255, null=True, verbose_name='Creator Agent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('creator', sitech_middlewares.fields.UserForeignKey(blank=True, db_column='created_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
        ),
    ]
