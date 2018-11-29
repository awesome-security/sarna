# coding: utf-8

from __future__ import absolute_import

from sarna.routes.api import util
from sarna.routes.api.models.base_model_ import Model


class FindingStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PENDING = "Pending"
    REVIEWED = "Reviewed"
    CONFIRMED = "Confirmed"
    FALSE_POSITIVE = "False_Positive"
    OTHER = "Other"

    def __init__(self):  # noqa: E501
        """FindingStatus - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'FindingStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FindingStatus of this FindingStatus.  # noqa: E501
        :rtype: FindingStatus
        """
        return util.deserialize_model(dikt, cls)
