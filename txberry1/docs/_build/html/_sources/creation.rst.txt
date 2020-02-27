Creation
========

#. Software:


.. code::

    pip install django
    Successfully installed asgiref-3.2.3 django-3.0.3 pytz-2019.3 sqlparse-0.3.0
    pip install djangorestframework
    Successfully installed djangorestframework-3.11.0

    django-admin startproject

    pip install mysqlclient
    Successfully installed mysqlclient-1.4.6

    python manage.py migrate
    python manage.py createsuperuser

    sudo apt  install httpie
    # or sudo apt install curl


#. Pizzas


From webpage: https://www.dagrasso.pl/menu
download page and images, and manually pick up IDs, names and stuffing to text file **from_dagrasso.txt**.
Every pizza starts with **<p class="product-desc">**.

Next convert file into objects with:

.. code::

    python manage.py shell
    from main.utils import create_from_dagrasso
    create_from_dagrasso.read()


image **pizza-formicetta.png** --> 20-1.png


