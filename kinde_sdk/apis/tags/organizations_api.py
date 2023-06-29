# coding: utf-8

"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""

from kinde_sdk.paths.api_v1_organizations_org_code_users.post import AddOrganizationUsers
from kinde_sdk.paths.api_v1_organization.post import CreateOrganization
from kinde_sdk.paths.api_v1_organizations_org_code_users_user_id_roles.post import CreateOrganizationUserRole
from kinde_sdk.paths.api_v1_organizations_org_code_feature_flags_feature_flag_key.delete import DeleteOrganizationFeatureFlagOverride
from kinde_sdk.paths.api_v1_organizations_org_code_feature_flags.delete import DeleteOrganizationFeatureFlagOverrides
from kinde_sdk.paths.api_v1_organizations_org_code_users_user_id_roles_role_id.delete import DeleteOrganizationUserRole
from kinde_sdk.paths.api_v1_organization.get import GetOrganization
from kinde_sdk.paths.api_v1_organizations_org_code_feature_flags.get import GetOrganizationFeatureFlags
from kinde_sdk.paths.api_v1_organizations_org_code_users_user_id_roles.get import GetOrganizationUserRoles
from kinde_sdk.paths.api_v1_organizations_org_code_users.get import GetOrganizationUsers
from kinde_sdk.paths.api_v1_organizations.get import GetOrganizations
from kinde_sdk.paths.api_v1_organizations_org_code_users_user_id.delete import RemoveOrganizationUser
from kinde_sdk.paths.api_v1_organization_org_code.patch import UpdateOrganization
from kinde_sdk.paths.api_v1_organizations_org_code_feature_flags_feature_flag_key.patch import UpdateOrganizationFeatureFlagOverride
from kinde_sdk.paths.api_v1_organizations_org_code_users.patch import UpdateOrganizationUsers


class OrganizationsApi(
    AddOrganizationUsers,
    CreateOrganization,
    CreateOrganizationUserRole,
    DeleteOrganizationFeatureFlagOverride,
    DeleteOrganizationFeatureFlagOverrides,
    DeleteOrganizationUserRole,
    GetOrganization,
    GetOrganizationFeatureFlags,
    GetOrganizationUserRoles,
    GetOrganizationUsers,
    GetOrganizations,
    RemoveOrganizationUser,
    UpdateOrganization,
    UpdateOrganizationFeatureFlagOverride,
    UpdateOrganizationUsers,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
