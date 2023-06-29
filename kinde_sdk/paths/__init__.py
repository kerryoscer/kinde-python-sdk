# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kinde_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    OAUTH2_USER_PROFILE = "/oauth2/user_profile"
    OAUTH2_V2_USER_PROFILE = "/oauth2/v2/user_profile"
    API_V1_USERS = "/api/v1/users"
    API_V1_USER = "/api/v1/user"
    API_V1_SUBSCRIBERS = "/api/v1/subscribers"
    API_V1_SUBSCRIBERS_SUBSCRIBER_ID = "/api/v1/subscribers/{subscriber_id}"
    API_V1_ORGANIZATION = "/api/v1/organization"
    API_V1_ORGANIZATION_ORG_CODE = "/api/v1/organization/{org_code}"
    API_V1_ORGANIZATIONS = "/api/v1/organizations"
    API_V1_ORGANIZATIONS_ORG_CODE_USERS = "/api/v1/organizations/{org_code}/users"
    API_V1_ORGANIZATIONS_ORG_CODE_USERS_USER_ID_ROLES = "/api/v1/organizations/{org_code}/users/{user_id}/roles"
    API_V1_ORGANIZATIONS_ORG_CODE_USERS_USER_ID_ROLES_ROLE_ID = "/api/v1/organizations/{org_code}/users/{user_id}/roles/{role_id}"
    API_V1_ORGANIZATIONS_ORG_CODE_USERS_USER_ID = "/api/v1/organizations/{org_code}/users/{user_id}"
    API_V1_CONNECTED_APPS_AUTH_URL = "/api/v1/connected_apps/auth_url"
    API_V1_CONNECTED_APPS_TOKEN = "/api/v1/connected_apps/token"
    API_V1_CONNECTED_APPS_REVOKE = "/api/v1/connected_apps/revoke"
    API_V1_FEATURE_FLAGS = "/api/v1/feature_flags"
    API_V1_FEATURE_FLAGS_FEATURE_FLAG_KEY = "/api/v1/feature_flags/{feature_flag_key}"
    API_V1_ORGANIZATIONS_ORG_CODE_FEATURE_FLAGS = "/api/v1/organizations/{org_code}/feature_flags"
    API_V1_ORGANIZATIONS_ORG_CODE_FEATURE_FLAGS_FEATURE_FLAG_KEY = "/api/v1/organizations/{org_code}/feature_flags/{feature_flag_key}"
    API_V1_ENVIRONMENT_FEATURE_FLAGS = "/api/v1/environment/feature_flags"
    API_V1_ENVIRONMENT_FEATURE_FLAGS_FEATURE_FLAG_KEY = "/api/v1/environment/feature_flags/{feature_flag_key}"
    API_V1_PERMISSIONS = "/api/v1/permissions"
    API_V1_PERMISSIONS_PERMISSION_ID = "/api/v1/permissions/{permission_id}"
    API_V1_ROLES = "/api/v1/roles"
    API_V1_ROLE = "/api/v1/role"
    API_V1_ROLES_ROLE_ID = "/api/v1/roles/{role_id}"
    API_V1_BUSINESS = "/api/v1/business"
    API_V1_INDUSTRIES = "/api/v1/industries"
    API_V1_TIMEZONES = "/api/v1/timezones"
    API_V1_APPLICATIONS_APP_ID_AUTH_REDIRECT_URLS = "/api/v1/applications/{app_id}/auth_redirect_urls"
