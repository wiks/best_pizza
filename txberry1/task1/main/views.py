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


def showall(request):
    """
    show all pizzass, toppings and images
    :param request:
    :return:
    """
    pizza_objs = Pizza.objects.all()
    topping_objs = Topping.objects.all()
    pizza_dict_list = []
    for pizza_obj in pizza_objs:
        topping_ids = json.loads(pizza_obj.toppings_ids_json)
        pizza_dict_list.append([
            pizza_obj,
            topping_ids,
        ])
    topping_dict_list = []
    for topping_obj in topping_objs:
        pizzas_ids = json.loads(topping_obj.pizzas_ids_json)
        topping_dict_list.append([
            topping_obj.id,
            topping_obj.name,
            pizzas_ids,
        ])
    web_context = {'pizzas': pizza_objs,
                   'toppings': topping_objs,
                   'pizza_dict_list': pizza_dict_list,
                   }
    response = render(request,
                      'showall.html',
                      web_context)
    return response


def results(request):
    """

    :param request:
    :return:
    """
    pizza_votes_objs = PizzaVotes.objects.all().order_by('order')
    topping_votes_objs = ToppingVotes.objects.all().order_by('order')
    kv = kval.KeyValue()
    web_context = {'pizzas_votes': pizza_votes_objs,
                   'toppings_votes': topping_votes_objs,
                   'pizza_order': kv.get_keyvalue('pizza_order'),
                   'topping_order': kv.get_keyvalue('topping_order'),
                   }
    response = render(request,
                      'results.html',
                      web_context)
    return response
