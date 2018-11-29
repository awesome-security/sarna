# coding: utf-8

from __future__ import absolute_import

from sarna.routes.api import util
from sarna.routes.api.models.base_model_ import Model


class OWASPCategory(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    INFO_001 = "OTG_INFO_001"
    INFO_002 = "OTG_INFO_002"
    INFO_003 = "OTG_INFO_003"
    INFO_004 = "OTG_INFO_004"
    INFO_005 = "OTG_INFO_005"
    INFO_006 = "OTG_INFO_006"
    INFO_007 = "OTG_INFO_007"
    INFO_008 = "OTG_INFO_008"
    INFO_009 = "OTG_INFO_009"
    INFO_010 = "OTG_INFO_010"
    CONFIG_001 = "OTG_CONFIG_001"
    CONFIG_002 = "OTG_CONFIG_002"
    CONFIG_003 = "OTG_CONFIG_003"
    CONFIG_004 = "OTG_CONFIG_004"
    CONFIG_005 = "OTG_CONFIG_005"
    CONFIG_006 = "OTG_CONFIG_006"
    CONFIG_007 = "OTG_CONFIG_007"
    CONFIG_008 = "OTG_CONFIG_008"
    IDENT_001 = "OTG_IDENT_001"
    IDENT_002 = "OTG_IDENT_002"
    IDENT_003 = "OTG_IDENT_003"
    IDENT_004 = "OTG_IDENT_004"
    IDENT_005 = "OTG_IDENT_005"
    IDENT_006 = "OTG_IDENT_006"
    IDENT_007 = "OTG_IDENT_007"
    AUTHN_001 = "OTG_AUTHN_001"
    AUTHN_002 = "OTG_AUTHN_002"
    AUTHN_003 = "OTG_AUTHN_003"
    AUTHN_004 = "OTG_AUTHN_004"
    AUTHN_005 = "OTG_AUTHN_005"
    AUTHN_006 = "OTG_AUTHN_006"
    AUTHN_007 = "OTG_AUTHN_007"
    AUTHN_008 = "OTG_AUTHN_008"
    AUTHN_009 = "OTG_AUTHN_009"
    AUTHN_010 = "OTG_AUTHN_010"
    AUTHZ_001 = "OTG_AUTHZ_001"
    AUTHZ_002 = "OTG_AUTHZ_002"
    AUTHZ_003 = "OTG_AUTHZ_003"
    AUTHZ_004 = "OTG_AUTHZ_004"
    SESS_001 = "OTG_SESS_001"
    SESS_002 = "OTG_SESS_002"
    SESS_003 = "OTG_SESS_003"
    SESS_004 = "OTG_SESS_004"
    SESS_005 = "OTG_SESS_005"
    SESS_006 = "OTG_SESS_006"
    SESS_007 = "OTG_SESS_007"
    SESS_008 = "OTG_SESS_008"
    INPVAL_001 = "OTG_INPVAL_001"
    INPVAL_002 = "OTG_INPVAL_002"
    INPVAL_003 = "OTG_INPVAL_003"
    INPVAL_004 = "OTG_INPVAL_004"
    INPVAL_005 = "OTG_INPVAL_005"
    INPVAL_006 = "OTG_INPVAL_006"
    INPVAL_007 = "OTG_INPVAL_007"
    INPVAL_008 = "OTG_INPVAL_008"
    INPVAL_009 = "OTG_INPVAL_009"
    INPVAL_010 = "OTG_INPVAL_010"
    INPVAL_011 = "OTG_INPVAL_011"
    INPVAL_012 = "OTG_INPVAL_012"
    INPVAL_013 = "OTG_INPVAL_013"
    INPVAL_014 = "OTG_INPVAL_014"
    INPVAL_015 = "OTG_INPVAL_015"
    INPVAL_016 = "OTG_INPVAL_016"
    ERR_001 = "OTG_ERR_001"
    ERR_002 = "OTG_ERR_002"
    CRYPST_001 = "OTG_CRYPST_001"
    CRYPST_002 = "OTG_CRYPST_002"
    CRYPST_003 = "OTG_CRYPST_003"
    BUSLOGIC_001 = "OTG_BUSLOGIC_001"
    BUSLOGIC_002 = "OTG_BUSLOGIC_002"
    BUSLOGIC_003 = "OTG_BUSLOGIC_003"
    BUSLOGIC_004 = "OTG_BUSLOGIC_004"
    BUSLOGIC_005 = "OTG_BUSLOGIC_005"
    BUSLOGIC_006 = "OTG_BUSLOGIC_006"
    BUSLOGIC_007 = "OTG_BUSLOGIC_007"
    BUSLOGIC_008 = "OTG_BUSLOGIC_008"
    BUSLOGIC_009 = "OTG_BUSLOGIC_009"
    CLIENT_001 = "OTG_CLIENT_001"
    CLIENT_002 = "OTG_CLIENT_002"
    CLIENT_003 = "OTG_CLIENT_003"
    CLIENT_004 = "OTG_CLIENT_004"
    CLIENT_005 = "OTG_CLIENT_005"
    CLIENT_006 = "OTG_CLIENT_006"
    CLIENT_007 = "OTG_CLIENT_007"
    CLIENT_008 = "OTG_CLIENT_008"
    CLIENT_009 = "OTG_CLIENT_009"
    CLIENT_010 = "OTG_CLIENT_010"
    CLIENT_011 = "OTG_CLIENT_011"
    CLIENT_012 = "OTG_CLIENT_012"

    def __init__(self):  # noqa: E501
        """OWASPCategory - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'OWASPCategory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OWASPCategory of this OWASPCategory.  # noqa: E501
        :rtype: OWASPCategory
        """
        return util.deserialize_model(dikt, cls)
