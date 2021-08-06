# Generated by Django 3.2 on 2021-07-27 20:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeSet',
            fields=[
                ('attribute_set_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('attribute_set_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('entity_type_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('entity_type_label', models.CharField(max_length=45)),
                ('entity_type_code', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_code', models.TextField()),
                ('role_label', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserEntity',
            fields=[
                ('user_entity_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=45, unique=True)),
                ('password', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('attribute_set_id', models.ForeignKey(db_column='attribute_set_id', on_delete=django.db.models.deletion.PROTECT, to='entities.attributeset', verbose_name='Attribute Set')),
            ],
        ),
        migrations.CreateModel(
            name='UserRoleAttribute',
            fields=[
                ('attribute_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('attribute_code', models.TextField()),
                ('frontend_label', models.TextField()),
                ('frontend_input', models.TextField()),
                ('attribute_type', models.TextField()),
                ('is_required', models.BooleanField()),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRoleEntityDataTypes',
            fields=[
                ('entity_data_type_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_type_code', models.TextField()),
                ('data_type_label', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('user_role_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_id', models.ForeignKey(db_column='role_id', on_delete=django.db.models.deletion.PROTECT, to='entities.roles', verbose_name='Role ID')),
                ('user_entity_id', models.ForeignKey(db_column='user_entity_id', on_delete=django.db.models.deletion.PROTECT, to='entities.userentity', verbose_name='User ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserRoleEntityData',
            fields=[
                ('entity_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attribute_set_id', models.ForeignKey(db_column='attribute_set_id', on_delete=django.db.models.deletion.PROTECT, to='entities.attributeset', verbose_name='Attribute Set')),
                ('entity_data_type_id', models.ForeignKey(db_column='entity_data_type_id', on_delete=django.db.models.deletion.CASCADE, to='entities.userroleentitydatatypes', verbose_name='role entity data record type.')),
                ('user_entity_id', models.ForeignKey(db_column='user_entity_id', on_delete=django.db.models.deletion.CASCADE, to='entities.userentity', verbose_name='User entity id')),
            ],
        ),
        migrations.CreateModel(
            name='UserRoleAttributeValues',
            fields=[
                ('value_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.TextField()),
                ('attribute_id', models.ForeignKey(db_column='attribute_id', on_delete=django.db.models.deletion.PROTECT, to='entities.userroleattribute', verbose_name='role entity attribute')),
                ('entity_id', models.ForeignKey(db_column='entity_id', on_delete=django.db.models.deletion.PROTECT, to='entities.userroleentitydata', verbose_name='role entity data ID')),
                ('entity_type_id', models.ForeignKey(db_column='entity_type_id', on_delete=django.db.models.deletion.PROTECT, to='entities.entitytype', verbose_name='role entity type')),
            ],
        ),
        migrations.CreateModel(
            name='RolePermissions',
            fields=[
                ('permission_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('operation_id', models.CharField(choices=[('CREATE', 'Create'), ('EDIT', 'Edit'), ('DELETE', 'Delete')], default='CREATE', max_length=10)),
                ('resource_entity_id', models.CharField(max_length=32)),
                ('entity_type_id', models.ForeignKey(db_column='entity_type_id', on_delete=django.db.models.deletion.PROTECT, to='entities.entitytype', verbose_name='Entity Type')),
                ('role_id', models.ForeignKey(db_column='role_id', on_delete=django.db.models.deletion.PROTECT, to='entities.roles', verbose_name='Role ID')),
            ],
        ),
        migrations.CreateModel(
            name='EntityUpdates',
            fields=[
                ('entity_update_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('entity_id', models.CharField(max_length=32)),
                ('updated_at', models.DateTimeField()),
                ('update_comments', models.TextField()),
                ('updated_user_id', models.CharField(max_length=32)),
                ('fields_updated', models.TextField()),
                ('entity_type_id', models.ForeignKey(db_column='entity_type_id', on_delete=django.db.models.deletion.PROTECT, to='entities.entitytype', verbose_name='Entity type')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeGroup',
            fields=[
                ('attribute_group_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('attribute_group_code', models.TextField()),
                ('attribute_group_name', models.TextField()),
                ('attribute_set_id', models.ForeignKey(db_column='attribute_set_id', on_delete=django.db.models.deletion.PROTECT, to='entities.attributeset', verbose_name='Attribute Set')),
            ],
        ),
    ]