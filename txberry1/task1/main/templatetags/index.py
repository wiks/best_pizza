#!/usr/bin/env python
# -*- coding: utf8 -*-

from django import template

register = template.Library()


@register.filter
def index(List, i):
    """
    https://stackoverflow.com/questions/4651172/reference-list-item-by-index-within-django-template/29664945#29664945
    {{ List|index:x|index:y }}
    :param List:
    :param i:
    :return:
    """
    index = int(i) % len(List)
    return List[index]

