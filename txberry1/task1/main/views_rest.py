#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import viewsets
from main.serializers import UserSerializer
from main.serializers import PizzaSerializer
from main.serializers import ToppingSerializer
from main.models import Pizza
from main.models import Topping
from main.models import PizzaVotes
from main.models import ToppingVotes
from main.utils import kval, pizza_tools
import logging

logger = logging.getLogger('debug')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PizzaViewSet(viewsets.ReadOnlyModelViewSet):
    """

    """
    queryset = Pizza.objects.all().order_by('id')
    serializer_class = PizzaSerializer


class ToppingViewSet(viewsets.ReadOnlyModelViewSet):
    """

    """
    queryset = Topping.objects.all().order_by('id')
    serializer_class = ToppingSerializer


def vote(request):
    """

    :param request:
    :param id:
    :return:
    """
    resp_dict = {'r': 'lipa',
                 }
    ask_dict = json.loads(request.body.decode('utf-8'))
    logger.debug('RX dict:  %s', ask_dict)
    if 'name' in ask_dict:
        pit = pizza_tools.PizzaTools()
        kv = kval.KeyValue()
        if ask_dict['name'] == 'pizza_vote':
            if 'pizza_id' in ask_dict:
                pizza_obj = Pizza.objects.filter(pk=int(ask_dict['pizza_id'])).first()
                if pizza_obj:
                    pizzaVotes_obj = PizzaVotes.objects.filter(pizza=pizza_obj).first()
                    if not pizzaVotes_obj:
                        pizzaVotes_obj = PizzaVotes()
                        pizzaVotes_obj.pizza = pizza_obj
                    pizzaVotes_obj.votes += 1
                    pizzaVotes_obj.dt = timezone.now()
                    pizzaVotes_obj.save()
                    most_liked_topping = []
                    toppings_ids_list = json.loads(pizza_obj.toppings_ids_json)
                    for topping_id in toppings_ids_list:
                        topping_obj = Topping.objects.filter(pk=topping_id).first()
                        topping_votes_obj = ToppingVotes.objects.filter(topping=topping_obj).first()
                        if not topping_votes_obj:
                            topping_votes_obj = ToppingVotes()
                            topping_votes_obj.topping = topping_obj
                        topping_votes_obj.votes += 1
                        topping_votes_obj.dt = timezone.now()
                        topping_votes_obj.save()
                    most_liked_toppings_list = ToppingVotes.objects.all().order_by('-votes')[:6]
                    for o in most_liked_toppings_list:
                        if o.topping.pk not in [1, ]:  # the first is 'ciasto' :-), and maybe exclude some of fillings
                            most_liked_topping.append(o.topping.name)
                    if pit.order_pizzas():
                        kv.keyvalue_setupdate('pizza_order', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    if pit.order_toppins():
                        kv.keyvalue_setupdate('topping_order', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    resp_dict = {'name': pizza_obj.name,
                                 'votes': pizzaVotes_obj.votes,
                                 'most_liked_topping': most_liked_topping,
                                 }
        if ask_dict['name'] == 'changes':
            pizza_votes_list = list(PizzaVotes.objects.all().order_by('order').values_list('pizza_id', flat=True))
            topping_votes_list = list(ToppingVotes.objects.all().order_by('order').values_list('topping_id', flat=True))
            resp_dict = {'pizza_order': kv.get_keyvalue('pizza_order'),
                         'topping_order': kv.get_keyvalue('topping_order'),
                         'pizza_list': pizza_votes_list,
                         'topping_list': topping_votes_list,
                         }
        if ask_dict['name'] == 'pizza-topping-podium':
            pvdl = PizzaVotes.objects.all().order_by('order')[:3]
            pizza_list = []
            for p in pvdl:
                pizza_list.append([p.pizza_id,
                                   p.pizza.name,
                                   '{:02d}-1.png'.format(p.pizza.web_id)
                                   ])
            resp_dict = {'pizza_order': kv.get_keyvalue('pizza_order'),
                         'pizza_list': pizza_list,
                         }
    # else:
    #     pass
    logger.debug('TX dict:  %s', resp_dict)
    response = JsonResponse(resp_dict)
    return response

