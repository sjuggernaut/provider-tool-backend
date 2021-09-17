from entities.helper import HttpResponse
from rest_framework import status
from entities.models import UserRoleEntityDataTypes, UserRoleEntityData, UserRoleAttribute, AttributeGroup, \
    AttributeSet, UserEntity
from django.db.utils import IntegrityError, Error
from django.core.exceptions import ValidationError
from providertool.constants import *
from datetime import datetime
from django.forms.models import model_to_dict
from userentity.serializers import *
from entities.helper import InputParser


class UserEntityDataTypesModel:
    def add_type(self, type_data):
        """
        Create a user entity data type record.
        :param type_data:
        :return:
        """
        try:
            if all(key not in type_data for key in API_ENTITY_DATA_TYPES_CREATE_REQUEST_BODY):
                return HttpResponse(result=False, message="Missing required request field values for entity data type.",
                                    status=status.HTTP_400_BAD_REQUEST)

            data_type_created = UserRoleEntityDataTypes()
            data_type_created.data_type_code = type_data.get("data_type_code")
            data_type_created.data_type_label = type_data.get("data_type_label")
            data_type_created.attribute_set_id = AttributeSet.objects.get(
                attribute_set_id=type_data.get('attribute_set'))
            data_type_created.save()

            return HttpResponse(result=True, message="Created User Entity Data type",
                                status=status.HTTP_200_OK, id_value=data_type_created.entity_data_type_id,
                                id="data_type_id")

        except ValidationError as ve:
            return HttpResponse(result=False,
                                message="Please provide a valid attribute set value.",
                                status=status.HTTP_400_BAD_REQUEST)

        except AttributeSet.DoesNotExist:
            return HttpResponse(result=False,
                                message="Invalid Attribute set value. Please provide a valid attribute set value to create data type.",
                                status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError as ie:
            ie_message = ie.args[1]
            if "Duplicate entry" in ie_message:
                ie_message = "The data type 'code' already exists. Could not create entity data type record."
            return HttpResponse(result=False, message=ie_message,
                                status=status.HTTP_400_BAD_REQUEST)

        except Error as e:
            return HttpResponse(result=False, message="Failed to created data type",
                                status=status.HTTP_400_BAD_REQUEST)

    def get_type_detail(self, data_type_id):
        try:
            response_json = UserRoleEntityDataTypes.objects.values().get(entity_data_type_id=data_type_id)
            return HttpResponse(result=True, message="Data type detail fetch success.", status=status.HTTP_200_OK,
                                value=response_json)
        except ValidationError:
            return HttpResponse(result=False, message="Invalid data type query parameter provided.",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except UserRoleEntityDataTypes.DoesNotExist as e:
            return HttpResponse(result=False, message="Data type detail does not exist.",
                                status=status.HTTP_200_OK)
        except Error as e:
            return HttpResponse(result=False, message="Failure to fetch Data type detail.",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list_data_types(self):
        try:
            response_json = UserRoleEntityDataTypes.objects.values()

            if len(response_json) > 0:
                return HttpResponse(result=True, message="Data types list generated successfully.",
                                    status=status.HTTP_200_OK,
                                    value=response_json)

            return HttpResponse(result=False, message="No Data types found.",
                                status=status.HTTP_200_OK)

        except Error as e:
            return HttpResponse(result=False, message="Failure to list data types.",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update_type_detail(self, data_type_id, data_type_detail):
        """
        Update Entity Data type detail
        Only permitted to update data_type_label, is_active, updated_at values.
        Not allowed to update data_type_code.
        :param data_type_id:
        :param data_type_detail:
        :return:
        """
        try:
            update_data_type = UserRoleEntityDataTypes.objects.get(entity_data_type_id=data_type_id)

            for attr, val in data_type_detail.items():
                if attr in API_ENTITY_DATA_TYPES_UPDATE_REQUEST_BODY:
                    setattr(update_data_type, attr, val)

            update_data_type.updated_at = datetime.now()
            update_data_type.save()
            return HttpResponse(result=True, message="Entity Data type detail update success.",
                                status=status.HTTP_200_OK)
        except Error as e:
            return HttpResponse(result=False, message="Failure to update entity data type detail.",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserEntityDataAttributesModel:

    def add_attribute(self, attribute_data):
        """
        Create a user entity attribute.
        :param attribute_data:
        :return:
        """
        try:
            if all(key not in attribute_data for key in API_ENTITY_ATTRIBUTE_CREATE_REQUEST_BODY):
                return HttpResponse(result=False, message="Missing required request field values for entity data type.",
                                    status=status.HTTP_400_BAD_REQUEST)

            attribute_created = UserRoleAttribute()
            attribute_created.attribute_code = attribute_data.get("attribute_code")
            attribute_created.attribute_type = attribute_data.get("attribute_type")
            attribute_created.frontend_label = attribute_data.get("frontend_label")
            attribute_created.frontend_input = attribute_data.get("frontend_input")
            attribute_created.is_required = attribute_data.get("is_required")
            attribute_created.note = attribute_data.get("note")
            attribute_created.is_active = True
            attribute_created.attribute_group = AttributeGroup.objects.get(
                attribute_group_id=attribute_data.get("attribute_group"))

            attribute_created.save()

            return HttpResponse(result=True, message="Created User Entity Data Attribute",
                                status=status.HTTP_200_OK, id_value=attribute_created.attribute_id,
                                id="attribute_id")

        except IntegrityError as ie:
            ie_message = ie.args[1]
            if "Duplicate entry" in ie_message:
                ie_message = "The data attribute 'code' already exists. Could not create entity data attribute record."
            return HttpResponse(result=False, message=ie_message,
                                status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as ve:
            return HttpResponse(result=False,
                                message="Please provide a valid attribute group value.",
                                status=status.HTTP_400_BAD_REQUEST)

        except AttributeGroup.DoesNotExist:
            return HttpResponse(result=False,
                                message="Invalid Attribute group value. Please provide a valid attribute group value to create attribute.",
                                status=status.HTTP_400_BAD_REQUEST)

        except Error as e:
            return HttpResponse(result=False, message="Failed to created entity data attribute",
                                status=status.HTTP_400_BAD_REQUEST)

    def list_attributes(self):
        try:
            response_json = UserRoleAttribute.objects.values()

            if len(response_json) > 0:
                return HttpResponse(result=True, message="Attribute list generated successfully.",
                                    status=status.HTTP_200_OK,
                                    value=response_json)

            return HttpResponse(result=False, message="No Attributes found.",
                                status=status.HTTP_200_OK)

        except Error as e:
            return HttpResponse(result=False, message="Failure to list attributes.",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list_attributes_by_attr_group(self, attr_group_id):
        try:
            response_json = UserRoleAttribute.objects.values().filter(attribute_group=attr_group_id)

            if len(response_json) > 0:
                return HttpResponse(result=True, message="Attribute list generated successfully.",
                                    status=status.HTTP_200_OK,
                                    value=response_json)

            return HttpResponse(result=False, message="No Attributes found.",
                                status=status.HTTP_200_OK)

        except ValidationError as ve:
            return HttpResponse(result=False,
                                message="Please provide a valid attribute group value.",
                                status=status.HTTP_400_BAD_REQUEST)

        except AttributeGroup.DoesNotExist:
            return HttpResponse(result=False,
                                message="Invalid Attribute group value provided.",
                                status=status.HTTP_400_BAD_REQUEST)

        except Error as e:
            return HttpResponse(result=False, message="Failure to list attributes.",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_attribute_detail(self, attribute_id):
        try:
            response_json = UserRoleAttribute.objects.values().get(attribute_id=attribute_id)
            return HttpResponse(result=True, message="Attribute detail fetch success.", status=status.HTTP_200_OK,
                                value=response_json)
        except ValidationError:
            return HttpResponse(result=False, message="Invalid attribute query parameter provided.",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except UserRoleAttribute.DoesNotExist as e:
            return HttpResponse(result=False, message="Attribute detail does not exist.",
                                status=status.HTTP_200_OK)
        except Error as e:
            return HttpResponse(result=False, message="Failure to fetch attribute detail.",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update_attribute(self, attribute_id, attribute_data):
        """
        Update User role entity attribute record.
        Only allowed to update frontend_label, note,
        :param attribute_id:
        :param attribute_data:
        :return:
        """
        try:
            update_attribute = UserRoleAttribute.objects.get(attribute_id=attribute_id)

            for attr, val in attribute_data.items():
                if attr in API_ENTITY_ATTRIBUTE_UPDATE_REQUEST_BODY:
                    setattr(update_attribute, attr, val)

            update_attribute.updated_at = datetime.now()
            update_attribute.save()
            return HttpResponse(result=True, message="Entity Data Attribute detail update success.",
                                status=status.HTTP_200_OK)

        except ValidationError as ve:
            return HttpResponse(result=False,
                                message="Please provide a valid attribute query value.",
                                status=status.HTTP_400_BAD_REQUEST)

        except UserRoleAttribute.DoesNotExist:
            return HttpResponse(result=False,
                                message="Invalid Attribute ID value. Please provide a valid attribute group value to update",
                                status=status.HTTP_400_BAD_REQUEST)

        except Error as e:
            return HttpResponse(result=False, message="Failure to update entity data attribute detail.",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list_attributes_by_data_type(self, data_type_id):
        """
        List all attributes by User Role Entity Data type.
        :param data_type_id: UserRoleEntityDataTypes
        :return:
        """
        try:
            attribute_set, group_by_attribute_group = self.get_role_attribute_groups(data_type_id)

            return HttpResponse(result=True,
                                message="Attributes list generated successfully.",
                                status=status.HTTP_200_OK,
                                value={
                                    "attribute_groups": group_by_attribute_group,
                                    "attribute_set": AttributeSetSerializer(attribute_set).data
                                })

        except ValidationError as ve:
            return HttpResponse(result=False,
                                message="Failure to fetch list of attributes. Please provide a valid data type value.",
                                status=status.HTTP_400_BAD_REQUEST)

        except UserRoleEntityDataTypes.DoesNotExist:
            # Handle data type get - matching query does not exist result.
            return HttpResponse(result=False,
                                message="Invalid data type query parameter value provided.",
                                status=status.HTTP_400_BAD_REQUEST)

    def get_role_attribute_groups(self, data_type_id):
        # 1 - Get UserRoleEntityDataTypes object by data_type_id
        data_type = UserRoleEntityDataTypes.objects.get(entity_data_type_id=data_type_id)
        request_attribute_set = data_type.attribute_set_id
        """
                    - Get All AttributeGroup objects that have parent attribute group empty ie. get only parent attr groups.
                    """
        request_attribute_groups = AttributeGroup.objects.filter(attribute_set_id=request_attribute_set,
                                                                 parent_attribute_group__isnull=True)
        attribute_set = AttributeSet.objects.get(attribute_set_id=request_attribute_set.attribute_set_id)
        group_by_attribute_group = {}
        # Iterate the attribute group.
        for attribute_group_item in request_attribute_groups:
            group_by_attribute_group[attribute_group_item.attribute_group_code] = {
                "default_attributes": UserRoleAttributeSerializer(
                    UserRoleAttribute.objects.filter(attribute_group=attribute_group_item,
                                                     is_active=True), many=True).data,
                "child_attribute_groups": {},
                "group_detail": AttributeGroupSerializer(attribute_group_item).data
            }

            group_dict = group_by_attribute_group[attribute_group_item.attribute_group_code]

            # each attribute group loop and filter other attribute groups by parent attr group
            children_attribute_groups = AttributeGroup.objects.filter(parent_attribute_group=attribute_group_item)

            children_attributes = UserRoleAttribute.objects.filter(attribute_group__in=children_attribute_groups,
                                                                   is_active=True)

            # add children attribute groups to the parent attribute group detail
            for child_group in children_attribute_groups:
                group_dict["child_attribute_groups"][child_group.attribute_group_code] = {
                    'attributes': [],
                    'group_detail': AttributeGroupSerializer(child_group).data
                }

            # loop all the attributes and put them into respective attribute group.
            for attribute_item in children_attributes:
                item_attr_group_code = attribute_item.attribute_group.attribute_group_code
                if item_attr_group_code in group_dict["child_attribute_groups"]:
                    group_dict.get('child_attribute_groups')[item_attr_group_code]['attributes'].append(
                        UserRoleAttributeSerializer(attribute_item).data)
                else:
                    group_dict.get('child_attribute_groups')[item_attr_group_code]['attributes'] = []
        return attribute_set, group_by_attribute_group

    def list_attributes_data_type_by_role(self, role_id):
        """
        List all attributes by User Role Entity Data type.
        :param data_type_id: UserRoleEntityDataTypes
        :return:
        """
        role_permission_resources = RolePermissions.objects.select_related('role_id', 'resource').filter(
            role_id=role_id).order_by('resource').values_list('resource').distinct()
        role_data_types = UserRoleEntityDataTypes.objects.values().filter(
            entity_data_type_id__in=role_permission_resources)
        result_role_data_type_attributes = {}

        if len(role_data_types) > 0:
            for data_type in role_data_types:
                data_type_id = data_type['entity_data_type_id']
                attribute_set, group_by_attribute_group = self.get_role_attribute_groups(data_type_id)
                result_role_data_type_attributes[str(data_type_id)] = {
                    "attribute_groups": group_by_attribute_group
                }

            return HttpResponse(result=True,
                                message="Attributes list generated successfully.",
                                status=status.HTTP_200_OK,
                                value={
                                    "data_type_attributes": result_role_data_type_attributes
                                })


class UserEntityDataModel:
    def create_data_attribute_values(self, entity_request_data, entity_data_record):
        try:
            if "attributes" in entity_request_data:
                attribute_keys_dict = entity_request_data.get('attributes').keys()
                attribute_query_set = UserRoleAttribute.objects.filter(attribute_id__in=attribute_keys_dict)

                attribute_request_data = entity_request_data.get('attributes')
                for attribute_item_id in attribute_request_data:
                    attribute_item_object = attribute_query_set.get(attribute_id=attribute_item_id)
                    attribute_model_type_column = ATTRIBUTE_TYPE_DICT.get(attribute_item_object.attribute_type,
                                                                          None)

                    """
                    Model Type OK - add attribute value record
                    """
                    if attribute_model_type_column:
                        attribute_request_value = attribute_request_data.get(attribute_item_id).get('value', None)
                        if attribute_request_value:
                            parsed_attribute_value = InputParser.parse_input(attribute_model_type_column,
                                                                             attribute_request_value)
                            attribute_value_record = AttributeValues()
                            attribute_value_record.attribute = attribute_item_object
                            attribute_value_record.entity_data_id = entity_data_record
                            setattr(attribute_value_record, attribute_model_type_column, parsed_attribute_value)
                            attribute_value_record.save()
                return True
        except ValidationError as ve:
            """
            Validation error if invalid attribute ID values are used in filter. 
            """
            print(ve)
            return False
        except Error as e:
            print(e)
            return False

    def add_data(self, entity_request_data):
        """
        Add a User Entity Data and create Value records for all the attributes.
        :param entity_request_data:
        :return:
        """
        try:
            if all(key not in entity_request_data for key in API_ENTITY_DATA_CREATE_REQUEST_BODY):
                return HttpResponse(result=False, message="Missing required request field values for entity data.",
                                    status=status.HTTP_400_BAD_REQUEST)

            # create Entity data record.
            entity_data_created = UserRoleEntityData()
            entity_data_created.entity_data_type_id = UserRoleEntityDataTypes.objects.get(
                entity_data_type_id=entity_request_data.get("data_type"))
            entity_data_created.user_entity_id = UserEntity.objects.get(
                user_entity_id=entity_request_data.get('user_id'))
            entity_data_created.save()

            # create attribute values tied to the entity data record.
            if self.create_data_attribute_values(entity_request_data, entity_data_created):
                return HttpResponse(result=True, message="Created Section data.",
                                    status=status.HTTP_200_OK, id_value=entity_data_created.entity_data_id,
                                    id="entity_data_id")
            else:
                entity_data_created.delete()
                return HttpResponse(result=True, message="Failed to create section data.",
                                    status=status.HTTP_200_OK)

        except UserEntity.DoesNotExist:
            return HttpResponse(result=False, message="Invalid user value provided.",
                                status=status.HTTP_400_BAD_REQUEST)

        except UserRoleEntityDataTypes.DoesNotExist:
            return HttpResponse(result=False, message="Invalid data type provided.",
                                status=status.HTTP_400_BAD_REQUEST)

        except Error as e:
            return HttpResponse(result=False, message="Failed to created entity data.",
                                status=status.HTTP_400_BAD_REQUEST)

    def list_data_by_user_id(self, user_id):
        try:
            user_role_entity_data = UserRoleEntityData.objects.filter(user_entity_id=user_id)

            if len(user_role_entity_data) > 0:
                refined_result = []
                for entity_data_item in user_role_entity_data:
                    user_id = entity_data_item.user_entity_id.user_entity_id
                    user_entity = UserEntity.objects.values().filter(user_entity_id=user_id)
                    user_role_entity_data_type = UserRoleEntityDataTypes.objects.values().filter(
                        entity_data_type_id=entity_data_item.entity_data_type_id.entity_data_type_id)

                    refined_result.append({
                        'entity_data': model_to_dict(entity_data_item),
                        'user': user_entity,
                        'data_type': user_role_entity_data_type
                    })

            if len(refined_result) > 0:
                return HttpResponse(result=True, message="User Entity Data generated successfully.",
                                    status=status.HTTP_200_OK,
                                    value=refined_result)

            return HttpResponse(result=False, message="No user entity data found.",
                                status=status.HTTP_200_OK)

        except Error as e:
            return HttpResponse(result=False, message="Failure to list user entity data.",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)