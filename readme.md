Create virtual environment with:
> mkvirtualenv django-basics

Then use the following command
> virtualenv --python=/usr/bin/python3.9 ~/.virtualenvs/django-basics/

to use latest version of python.
Install requirements with:
> pip install -r requirements.txt

## To create a project use command:
> django-admin startproject <project_name>

## To start a development server, enter your project folder and use the following command:
> python manage.py runserver
 
## To add an app to your project use:
> python manage.py startapp <app_name>
