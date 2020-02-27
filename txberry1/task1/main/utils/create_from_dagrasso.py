#!/usr/bin/env python
# -*- coding: utf8 -*-

'''



'''

import os
from django.conf import settings
from main.models import Pizza, PizzaVotes, Topping, ToppingVotes
import json
import logging

logger = logging.getLogger('debug')


def read():
    """

    :return:
    """

    with open(os.path.join(settings.BASE_DIR, 'main', 'utils', 'from_dagrasso.txt')) as f:
        fl = f.readlines()
        pairs = int(len(fl) / 2)
        for pair_index in range(pairs):
            first_line = fl[pair_index * 2].replace('\n','')
            second_line = fl[pair_index * 2 + 1].replace('\n','')
            web_id = int(first_line.split(' ', 1)[0])
            name = first_line.split(' ', 1)[1]
            topping_list = [x.strip(' ') for x in second_line.split(',')]

            # Pizza create or update
            pizza_obj = Pizza.objects.filter(name=name).first()
            if not pizza_obj:
                pizza_obj = Pizza()
                pizza_obj.web_id = web_id
                pizza_obj.name = name
                pizza_obj.save()
                pizza_votes_obj = PizzaVotes()
                pizza_votes_obj.pizza = pizza_obj
                pizza_votes_obj.save()

            topics_id_list = []
            for topping_one in topping_list:
                # Topping create or get
                topping_obj = Topping.objects.filter(name=topping_one).first()
                if not topping_obj:
                    topping_obj = Topping()
                    topping_obj.name = topping_one
                    topping_obj.pizzas_ids_json = json.dumps([pizza_obj.id])
                    topping_votes_obj = ToppingVotes()
                    topping_votes_obj.topping = topping_obj
                    topping_votes_obj.save()
                else:
                    pizzas_ids = json.loads(topping_obj.pizzas_ids_json)
                    if pizza_obj.id not in pizzas_ids:
                        pizzas_ids.append(pizza_obj.id)

                    topping_obj.pizzas_ids_json = json.dumps(pizzas_ids)
                topping_obj.save()
                topics_id_list.append(topping_obj.id)
            pizza_obj.toppings_ids_json = json.dumps(topics_id_list)
            pizza_obj.save()

            logger.debug('%s %s --> %s', web_id, name, topping_list)


'''
python3 manage.py shell
from main.utils import create_from_dagrasso
create_from_dagrasso.read()
exit()
'''
