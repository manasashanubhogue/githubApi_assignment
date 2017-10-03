# githubApi_assignment
Using https://developer.github.com/v3/ , create Api to search github user and store their data in database. 
Filter user and other params in admin panel, 
Test cases to be written, 
Generate report in admin panel.

pip install virtualenv

virtualenv venv

source venv/bin/activate

pip install django

pip install requests

django-admin startproject git_assignment

cd git_assignment/

python manage.py runserver

python manage.py migrate

python manage.py startapp user_profile

Follow https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04 to connect mysql to django app
