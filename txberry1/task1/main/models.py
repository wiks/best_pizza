#!/usr/bin/env python
# -*- coding: utf8 -*-

from django.db import models
from django.utils import timezone


class Pizza(models.Model):
    """

    """
    web_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=200)  # TODO utf8_polish_ci
    toppings_ids_json = models.TextField(default=None, blank=True, null=True)  # limit 4GB

    def __str__(self):
        return self.name


class Topping(models.Model):
    """

    """
    name = models.CharField(unique=True, max_length=200)  # TODO utf8_polish_ci
    pizzas_ids_json = models.TextField(default=None, blank=True, null=True)  # limit 4GB

    def __str__(self):
        return self.name


class PizzaVotes(models.Model):
    """

    """
    pizza = models.OneToOneField(
        Pizza,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    votes = models.IntegerField(default=0)
    order = models.IntegerField(default=None, blank=True, null=True)
    dt = models.DateTimeField()


class ToppingVotes(models.Model):
    """

    """
    topping = models.OneToOneField(
        Topping,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    votes = models.IntegerField(default=0)
    order = models.IntegerField(default=None, blank=True, null=True)
    dt = models.DateTimeField()


class KeyValues(models.Model):
    """

    """
    key = models.CharField(max_length=40, blank=True, null=True)
    value = models.TextField(default=None, blank=True, null=True)  # limit 4GB
    dt = models.DateTimeField(default=timezone.now)

