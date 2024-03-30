# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Geocache(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, enable: bool=None, connect_id: str=None, max_tiles_per_goal: int=None, max_size_of_cache_in_mb: int=None, cache_dir: str=None, num_threads: int=None):  # noqa: E501
        """Geocache - a model defined in Swagger

        :param enable: The enable of this Geocache.  # noqa: E501
        :type enable: bool
        :param connect_id: The connect_id of this Geocache.  # noqa: E501
        :type connect_id: str
        :param max_tiles_per_goal: The max_tiles_per_goal of this Geocache.  # noqa: E501
        :type max_tiles_per_goal: int
        :param max_size_of_cache_in_mb: The max_size_of_cache_in_mb of this Geocache.  # noqa: E501
        :type max_size_of_cache_in_mb: int
        :param cache_dir: The cache_dir of this Geocache.  # noqa: E501
        :type cache_dir: str
        :param num_threads: The num_threads of this Geocache.  # noqa: E501
        :type num_threads: int
        """
        self.swagger_types = {
            'enable': bool,
            'connect_id': str,
            'max_tiles_per_goal': int,
            'max_size_of_cache_in_mb': int,
            'cache_dir': str,
            'num_threads': int
        }

        self.attribute_map = {
            'enable': 'enable',
            'connect_id': 'connectId',
            'max_tiles_per_goal': 'maxTilesPerGoal',
            'max_size_of_cache_in_mb': 'maxSizeOfCacheInMb',
            'cache_dir': 'cacheDir',
            'num_threads': 'numThreads'
        }
        self._enable = enable
        self._connect_id = connect_id
        self._max_tiles_per_goal = max_tiles_per_goal
        self._max_size_of_cache_in_mb = max_size_of_cache_in_mb
        self._cache_dir = cache_dir
        self._num_threads = num_threads

    @classmethod
    def from_dict(cls, dikt) -> 'Geocache':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Geocache of this Geocache.  # noqa: E501
        :rtype: Geocache
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enable(self) -> bool:
        """Gets the enable of this Geocache.


        :return: The enable of this Geocache.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable: bool):
        """Sets the enable of this Geocache.


        :param enable: The enable of this Geocache.
        :type enable: bool
        """

        self._enable = enable

    @property
    def connect_id(self) -> str:
        """Gets the connect_id of this Geocache.


        :return: The connect_id of this Geocache.
        :rtype: str
        """
        return self._connect_id

    @connect_id.setter
    def connect_id(self, connect_id: str):
        """Sets the connect_id of this Geocache.


        :param connect_id: The connect_id of this Geocache.
        :type connect_id: str
        """

        self._connect_id = connect_id

    @property
    def max_tiles_per_goal(self) -> int:
        """Gets the max_tiles_per_goal of this Geocache.


        :return: The max_tiles_per_goal of this Geocache.
        :rtype: int
        """
        return self._max_tiles_per_goal

    @max_tiles_per_goal.setter
    def max_tiles_per_goal(self, max_tiles_per_goal: int):
        """Sets the max_tiles_per_goal of this Geocache.


        :param max_tiles_per_goal: The max_tiles_per_goal of this Geocache.
        :type max_tiles_per_goal: int
        """

        self._max_tiles_per_goal = max_tiles_per_goal

    @property
    def max_size_of_cache_in_mb(self) -> int:
        """Gets the max_size_of_cache_in_mb of this Geocache.


        :return: The max_size_of_cache_in_mb of this Geocache.
        :rtype: int
        """
        return self._max_size_of_cache_in_mb

    @max_size_of_cache_in_mb.setter
    def max_size_of_cache_in_mb(self, max_size_of_cache_in_mb: int):
        """Sets the max_size_of_cache_in_mb of this Geocache.


        :param max_size_of_cache_in_mb: The max_size_of_cache_in_mb of this Geocache.
        :type max_size_of_cache_in_mb: int
        """

        self._max_size_of_cache_in_mb = max_size_of_cache_in_mb

    @property
    def cache_dir(self) -> str:
        """Gets the cache_dir of this Geocache.


        :return: The cache_dir of this Geocache.
        :rtype: str
        """
        return self._cache_dir

    @cache_dir.setter
    def cache_dir(self, cache_dir: str):
        """Sets the cache_dir of this Geocache.


        :param cache_dir: The cache_dir of this Geocache.
        :type cache_dir: str
        """

        self._cache_dir = cache_dir

    @property
    def num_threads(self) -> int:
        """Gets the num_threads of this Geocache.


        :return: The num_threads of this Geocache.
        :rtype: int
        """
        return self._num_threads

    @num_threads.setter
    def num_threads(self, num_threads: int):
        """Sets the num_threads of this Geocache.


        :param num_threads: The num_threads of this Geocache.
        :type num_threads: int
        """

        self._num_threads = num_threads