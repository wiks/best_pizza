# best_pizza

1. installation
pip install django
Successfully installed asgiref-3.2.3 django-3.0.3 pytz-2019.3 sqlparse-0.3.0
pip install djangorestframework
Successfully installed djangorestframework-3.11.0
django-admin startproject
pip install mysqlclient
Successfully installed mysqlclient-1.4.6
python manage.py migrate
python manage.py createsuperuser
sudo apt install curl
sudo apt  install httpie
--------------------------------------------------------
2. create DBase
mysql -u root -p
CREATE DATABASE xberry;
GRANT ALL PRIVILEGES ON xberry.* TO 'xberry'@'localhost' IDENTIFIED BY '4Alay9ilenceihhc';
FLUSH PRIVILEGES;
exit;
--------------------------------------------------------
3. create pizza`s dbase content:

source venv/bin/activate

python3 manage.py shell
from main.utils import create_from_dagrasso
create_from_dagrasso.read()
exit()
--------------------------------------------------------
4. run:
python3 manage.py runserver

