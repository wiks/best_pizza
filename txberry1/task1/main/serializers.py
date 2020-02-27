#!/usr/bin/env python
# -*- coding: utf8 -*-

from django.contrib.auth.models import User
from main.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ['url', 'name']


class ToppingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topping
        fields = ['url', 'name']
