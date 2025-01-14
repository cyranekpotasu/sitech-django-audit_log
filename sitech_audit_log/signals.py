from django.db.models.signals import post_save, post_delete
from sitech_audit_log import AuditLog, AuditLogMixin
from sitech_middlewares.request import get_current_request, get_current_user
from sitech_audit_log.utils import get_user_agent, get_user_ip
from django.db import connections


def _post_save_handler(sender, instance, created, using, **kwargs):
    if isinstance(instance, AuditLogMixin):
        operation = "created" if created else "updated"
        if operation in instance.log_operations:
            values = _get_dirty_values(instance, operation, using)
            if values:
                request = get_current_request()
                user = get_current_user()
                if not user.is_anonymous:
                    user_ip = get_user_ip(request)
                    user_agent = get_user_agent(request)

                    AuditLog().set_auditable(instance).set_operation(operation).set_values(values).set_creator(
                        user).set_creator_agent(user_agent).set_creator_ip(user_ip).save()


def _post_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, AuditLogMixin):
        operation = "deleted"
        if operation in instance.log_operations:
            values = _get_dirty_values(instance, operation, using)
            if values:
                request = get_current_request()
                user = get_current_user()
                if not user.is_anonymous:
                    user_ip = get_user_ip(request)
                    user_agent = get_user_agent(request)

                    AuditLog().set_auditable(instance).set_operation(operation).set_values(values).set_creator(
                        user).set_creator_agent(user_agent).set_creator_ip(user_ip).save()

def _get_dirty_values(instance, operation, using):
    values = []
    if isinstance(instance, AuditLogMixin):
        for field in instance._meta.fields:
            attname, column = field.get_attname_column()
            if operation == 'deleted' or (field.name not in instance.ignore_changed_fields and instance._old_fields[attname] != getattr(instance, attname)):
                field_value = {
                    'att': attname,
                    'value': field.get_db_prep_value(getattr(instance, attname), connections[using]),
                }
                if operation == 'updated':
                    field_value['old_value'] = field.get_db_prep_value(instance._old_fields[attname], connections[using])
                values.append(field_value)
    return values

post_save.connect(_post_save_handler)
post_delete.connect(_post_delete_handler)
