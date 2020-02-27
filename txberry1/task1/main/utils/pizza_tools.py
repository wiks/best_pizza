#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
from django.shortcuts import render
from main.models import Pizza
from main.models import Topping
from main.models import PizzaVotes
from main.models import ToppingVotes
from main.utils import kval
import logging

logger = logging.getLogger('debug')

class PizzaTools:
    """

    """

    def order_pizzas(self):
        """

        :return:
        """
        pizza_order_changed = False
        pizzaVotes_ordered_objs = PizzaVotes.objects.all().order_by('-votes')
        index = 1
        for pizzaVotes_ordered_obj in pizzaVotes_ordered_objs:
            if pizzaVotes_ordered_obj.order != index:
                pizza_order_changed = True
            pizzaVotes_ordered_obj.order = index
            pizzaVotes_ordered_obj.save()
            index += 1
        return pizza_order_changed

    def order_toppins(self):
        """

        :return:
        """
        toppings_order_changed = False
        toppingVotes_ordered_objs = ToppingVotes.objects.all().order_by('-votes')
        index = 1
        for toppingVotes_ordered_obj in toppingVotes_ordered_objs:
            if toppingVotes_ordered_obj.order != index:
                toppings_order_changed = True
            toppingVotes_ordered_obj.order = index
            toppingVotes_ordered_obj.save()
            index += 1
        return toppings_order_changed
