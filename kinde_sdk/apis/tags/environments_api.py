# coding: utf-8

"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""

from kinde_sdk.paths.api_v1_environment_feature_flags_feature_flag_key.delete import DeleteEnvironementFeatureFlagOverride
from kinde_sdk.paths.api_v1_environment_feature_flags.delete import DeleteEnvironementFeatureFlagOverrides
from kinde_sdk.paths.api_v1_environment_feature_flags.get import GetEnvironementFeatureFlags
from kinde_sdk.paths.api_v1_environment_feature_flags_feature_flag_key.patch import UpdateEnvironementFeatureFlagOverride


class EnvironmentsApi(
    DeleteEnvironementFeatureFlagOverride,
    DeleteEnvironementFeatureFlagOverrides,
    GetEnvironementFeatureFlags,
    UpdateEnvironementFeatureFlagOverride,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
