#!/usr/bin/env python
# -*- coding: utf8 -*-

from django.utils import timezone
# from datetime import datetime
# from dateutil import tz
# import pytz
# from django.conf import settings
# from django.contrib.auth.models import User
from main.models import KeyValues
import logging


class KeyValue:
    """

    """

    def __init__(self):
        """

        """
        self.logger = logging.getLogger('debug')

    def keyvalue_setupdate(self,
                           key,
                           value,
                           ):
        """

        :param ratequestion_id:
        :param key:
        :param value:
        :return:
        """
        kv = KeyValues.objects.filter(key=key
                                      ).first()
        if not kv:
            kv = KeyValues()
            kv.key = key
        kv.value = value
        kv.dt = timezone.now()
        kv.save()
        return None

    def get_keyvalue(self,
                     key,
                     default=None,
                     ):
        """

        :param key:
        :param user_id:
        :return:
        """
        value = None
        kv = KeyValues.objects.filter(key=key
                                      ).first()
        if kv:
            value = kv.value
        if not kv and default:
            kv = KeyValues()
            kv.key=key
            kv.value=default
            kv.dt=timezone.now()
            kv.save()
            value = kv.value
        return value

