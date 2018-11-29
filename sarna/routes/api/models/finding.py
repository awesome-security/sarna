# coding: utf-8

from __future__ import absolute_import

from sarna.routes.api import util
from sarna.routes.api.models import FindingTemplateResume, FindingStatus, FindingType, OWASPCategory, \
    OWASPMobileTop10Category, OWISAMCategory, Score
from sarna.routes.api.models.base_model_ import Model


class Finding(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, template=None, title=None, status=None, type=None, owasp_category=None, owasp_mobile_category=None, owisam_category=None, tech_risk=None, business_risk=None, exploitability=None, dissemination=None, solution_complexity=None, description=None, solution=None, definition=None, references=None, cvss_v3_vector=None):  # noqa: E501
        """Finding - a model defined in OpenAPI

        :param id: The id of this Finding.  # noqa: E501
        :type id: int
        :param name: The name of this Finding.  # noqa: E501
        :type name: str
        :param template: The template of this Finding.  # noqa: E501
        :type template: FindingTemplateResume
        :param title: The title of this Finding.  # noqa: E501
        :type title: str
        :param status: The status of this Finding.  # noqa: E501
        :type status: FindingStatus
        :param type: The type of this Finding.  # noqa: E501
        :type type: FindingType
        :param owasp_category: The owasp_category of this Finding.  # noqa: E501
        :type owasp_category: OWASPCategory
        :param owasp_mobile_category: The owasp_mobile_category of this Finding.  # noqa: E501
        :type owasp_mobile_category: OWASPMobileTop10Category
        :param owisam_category: The owisam_category of this Finding.  # noqa: E501
        :type owisam_category: OWISAMCategory
        :param tech_risk: The tech_risk of this Finding.  # noqa: E501
        :type tech_risk: Score
        :param business_risk: The business_risk of this Finding.  # noqa: E501
        :type business_risk: Score
        :param exploitability: The exploitability of this Finding.  # noqa: E501
        :type exploitability: Score
        :param dissemination: The dissemination of this Finding.  # noqa: E501
        :type dissemination: Score
        :param solution_complexity: The solution_complexity of this Finding.  # noqa: E501
        :type solution_complexity: Score
        :param description: The description of this Finding.  # noqa: E501
        :type description: str
        :param solution: The solution of this Finding.  # noqa: E501
        :type solution: str
        :param definition: The definition of this Finding.  # noqa: E501
        :type definition: str
        :param references: The references of this Finding.  # noqa: E501
        :type references: str
        :param cvss_v3_vector: The cvss_v3_vector of this Finding.  # noqa: E501
        :type cvss_v3_vector: str
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'template': FindingTemplateResume,
            'title': str,
            'status': FindingStatus,
            'type': FindingType,
            'owasp_category': OWASPCategory,
            'owasp_mobile_category': OWASPMobileTop10Category,
            'owisam_category': OWISAMCategory,
            'tech_risk': Score,
            'business_risk': Score,
            'exploitability': Score,
            'dissemination': Score,
            'solution_complexity': Score,
            'description': str,
            'solution': str,
            'definition': str,
            'references': str,
            'cvss_v3_vector': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'template': 'template',
            'title': 'title',
            'status': 'status',
            'type': 'type',
            'owasp_category': 'owasp_category',
            'owasp_mobile_category': 'owasp_mobile_category',
            'owisam_category': 'owisam_category',
            'tech_risk': 'tech_risk',
            'business_risk': 'business_risk',
            'exploitability': 'exploitability',
            'dissemination': 'dissemination',
            'solution_complexity': 'solution_complexity',
            'description': 'description',
            'solution': 'solution',
            'definition': 'definition',
            'references': 'references',
            'cvss_v3_vector': 'cvss_v3_vector'
        }

        self._id = id
        self._name = name
        self._template = template
        self._title = title
        self._status = status
        self._type = type
        self._owasp_category = owasp_category
        self._owasp_mobile_category = owasp_mobile_category
        self._owisam_category = owisam_category
        self._tech_risk = tech_risk
        self._business_risk = business_risk
        self._exploitability = exploitability
        self._dissemination = dissemination
        self._solution_complexity = solution_complexity
        self._description = description
        self._solution = solution
        self._definition = definition
        self._references = references
        self._cvss_v3_vector = cvss_v3_vector

    @classmethod
    def from_dict(cls, dikt) -> 'Finding':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Finding of this Finding.  # noqa: E501
        :rtype: Finding
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Finding.


        :return: The id of this Finding.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Finding.


        :param id: The id of this Finding.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Finding.


        :return: The name of this Finding.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Finding.


        :param name: The name of this Finding.
        :type name: str
        """
        if name is not None and len(name) > 60:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `60`")  # noqa: E501

        self._name = name

    @property
    def template(self):
        """Gets the template of this Finding.


        :return: The template of this Finding.
        :rtype: FindingTemplateResume
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Finding.


        :param template: The template of this Finding.
        :type template: FindingTemplateResume
        """

        self._template = template

    @property
    def title(self):
        """Gets the title of this Finding.


        :return: The title of this Finding.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Finding.


        :param title: The title of this Finding.
        :type title: str
        """
        if title is not None and len(title) > 128:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `128`")  # noqa: E501

        self._title = title

    @property
    def status(self):
        """Gets the status of this Finding.


        :return: The status of this Finding.
        :rtype: FindingStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Finding.


        :param status: The status of this Finding.
        :type status: FindingStatus
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this Finding.


        :return: The type of this Finding.
        :rtype: FindingType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Finding.


        :param type: The type of this Finding.
        :type type: FindingType
        """

        self._type = type

    @property
    def owasp_category(self):
        """Gets the owasp_category of this Finding.


        :return: The owasp_category of this Finding.
        :rtype: OWASPCategory
        """
        return self._owasp_category

    @owasp_category.setter
    def owasp_category(self, owasp_category):
        """Sets the owasp_category of this Finding.


        :param owasp_category: The owasp_category of this Finding.
        :type owasp_category: OWASPCategory
        """

        self._owasp_category = owasp_category

    @property
    def owasp_mobile_category(self):
        """Gets the owasp_mobile_category of this Finding.


        :return: The owasp_mobile_category of this Finding.
        :rtype: OWASPMobileTop10Category
        """
        return self._owasp_mobile_category

    @owasp_mobile_category.setter
    def owasp_mobile_category(self, owasp_mobile_category):
        """Sets the owasp_mobile_category of this Finding.


        :param owasp_mobile_category: The owasp_mobile_category of this Finding.
        :type owasp_mobile_category: OWASPMobileTop10Category
        """

        self._owasp_mobile_category = owasp_mobile_category

    @property
    def owisam_category(self):
        """Gets the owisam_category of this Finding.


        :return: The owisam_category of this Finding.
        :rtype: OWISAMCategory
        """
        return self._owisam_category

    @owisam_category.setter
    def owisam_category(self, owisam_category):
        """Sets the owisam_category of this Finding.


        :param owisam_category: The owisam_category of this Finding.
        :type owisam_category: OWISAMCategory
        """

        self._owisam_category = owisam_category

    @property
    def tech_risk(self):
        """Gets the tech_risk of this Finding.


        :return: The tech_risk of this Finding.
        :rtype: Score
        """
        return self._tech_risk

    @tech_risk.setter
    def tech_risk(self, tech_risk):
        """Sets the tech_risk of this Finding.


        :param tech_risk: The tech_risk of this Finding.
        :type tech_risk: Score
        """

        self._tech_risk = tech_risk

    @property
    def business_risk(self):
        """Gets the business_risk of this Finding.


        :return: The business_risk of this Finding.
        :rtype: Score
        """
        return self._business_risk

    @business_risk.setter
    def business_risk(self, business_risk):
        """Sets the business_risk of this Finding.


        :param business_risk: The business_risk of this Finding.
        :type business_risk: Score
        """

        self._business_risk = business_risk

    @property
    def exploitability(self):
        """Gets the exploitability of this Finding.


        :return: The exploitability of this Finding.
        :rtype: Score
        """
        return self._exploitability

    @exploitability.setter
    def exploitability(self, exploitability):
        """Sets the exploitability of this Finding.


        :param exploitability: The exploitability of this Finding.
        :type exploitability: Score
        """

        self._exploitability = exploitability

    @property
    def dissemination(self):
        """Gets the dissemination of this Finding.


        :return: The dissemination of this Finding.
        :rtype: Score
        """
        return self._dissemination

    @dissemination.setter
    def dissemination(self, dissemination):
        """Sets the dissemination of this Finding.


        :param dissemination: The dissemination of this Finding.
        :type dissemination: Score
        """

        self._dissemination = dissemination

    @property
    def solution_complexity(self):
        """Gets the solution_complexity of this Finding.


        :return: The solution_complexity of this Finding.
        :rtype: Score
        """
        return self._solution_complexity

    @solution_complexity.setter
    def solution_complexity(self, solution_complexity):
        """Sets the solution_complexity of this Finding.


        :param solution_complexity: The solution_complexity of this Finding.
        :type solution_complexity: Score
        """

        self._solution_complexity = solution_complexity

    @property
    def description(self):
        """Gets the description of this Finding.


        :return: The description of this Finding.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Finding.


        :param description: The description of this Finding.
        :type description: str
        """

        self._description = description

    @property
    def solution(self):
        """Gets the solution of this Finding.


        :return: The solution of this Finding.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        """Sets the solution of this Finding.


        :param solution: The solution of this Finding.
        :type solution: str
        """

        self._solution = solution

    @property
    def definition(self):
        """Gets the definition of this Finding.


        :return: The definition of this Finding.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this Finding.


        :param definition: The definition of this Finding.
        :type definition: str
        """

        self._definition = definition

    @property
    def references(self):
        """Gets the references of this Finding.


        :return: The references of this Finding.
        :rtype: str
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this Finding.


        :param references: The references of this Finding.
        :type references: str
        """

        self._references = references

    @property
    def cvss_v3_vector(self):
        """Gets the cvss_v3_vector of this Finding.


        :return: The cvss_v3_vector of this Finding.
        :rtype: str
        """
        return self._cvss_v3_vector

    @cvss_v3_vector.setter
    def cvss_v3_vector(self, cvss_v3_vector):
        """Sets the cvss_v3_vector of this Finding.


        :param cvss_v3_vector: The cvss_v3_vector of this Finding.
        :type cvss_v3_vector: str
        """
        if cvss_v3_vector is not None and len(cvss_v3_vector) > 128:
            raise ValueError("Invalid value for `cvss_v3_vector`, length must be less than or equal to `128`")  # noqa: E501

        self._cvss_v3_vector = cvss_v3_vector
