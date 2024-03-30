# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ConnectionInfoCertSubjectX500Principal(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, encoded: List[bytearray]=None):  # noqa: E501
        """ConnectionInfoCertSubjectX500Principal - a model defined in Swagger

        :param name: The name of this ConnectionInfoCertSubjectX500Principal.  # noqa: E501
        :type name: str
        :param encoded: The encoded of this ConnectionInfoCertSubjectX500Principal.  # noqa: E501
        :type encoded: List[bytearray]
        """
        self.swagger_types = {
            'name': str,
            'encoded': List[bytearray]
        }

        self.attribute_map = {
            'name': 'name',
            'encoded': 'encoded'
        }
        self._name = name
        self._encoded = encoded

    @classmethod
    def from_dict(cls, dikt) -> 'ConnectionInfoCertSubjectX500Principal':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ConnectionInfo_cert_subjectX500Principal of this ConnectionInfoCertSubjectX500Principal.  # noqa: E501
        :rtype: ConnectionInfoCertSubjectX500Principal
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ConnectionInfoCertSubjectX500Principal.


        :return: The name of this ConnectionInfoCertSubjectX500Principal.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ConnectionInfoCertSubjectX500Principal.


        :param name: The name of this ConnectionInfoCertSubjectX500Principal.
        :type name: str
        """

        self._name = name

    @property
    def encoded(self) -> List[bytearray]:
        """Gets the encoded of this ConnectionInfoCertSubjectX500Principal.


        :return: The encoded of this ConnectionInfoCertSubjectX500Principal.
        :rtype: List[bytearray]
        """
        return self._encoded

    @encoded.setter
    def encoded(self, encoded: List[bytearray]):
        """Sets the encoded of this ConnectionInfoCertSubjectX500Principal.


        :param encoded: The encoded of this ConnectionInfoCertSubjectX500Principal.
        :type encoded: List[bytearray]
        """

        self._encoded = encoded