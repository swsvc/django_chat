### Django chat application

This application was written as a test project.
However it will be extended further, so it may contain some features that are beyond original specification,
but not completed yet.

Project follows organization approach from "Two scoops of django" book.

Works on Python 3.6

Database used - PostgreSQL

Configuration files are separated (DJANGO_SETTINGS_MODULE):

- base - base config file that is extended by all other config files
- development - config file for local development
- production - config file for production
- testing - config file for testing

##### Modules

- Module: chat - main module of application
- Module: core - contains some base classes and templates. (For now it contains only base html templates
 for other templates to extend and auth mixins)
- Module: history - module for storing all messages (Not completed, will be extended significantly)
- Module: static - contains static files for project (css, js, img)

##### Project installation

Here I assume that development environment is separated using virtualenv,
which is created using virtualenv or virtualenvwrapper application.
Both these utilities create virtual environment with initialization scripts. For example, virtualenvwrapper
creates postactivate script, that resides in `<virtualenv>/bin` directory.

- checkout this repo
- create virtualenv

```
mkvirtualenv django_chat
```

In Pycharm (Community edition) it sometimes does not initialize the virtualenv correctly in console. So

```
deactivate
workon django_chat
```

- install requirements.txt

`pip install -r requirements.txt`

- add environment variables for this project into postactivate script of virtualenv

This approach prevents leaking secret keys to repository

```
export DJANGO_SETTINGS_MODULE=django_chat.settings.development
... and so on
```

To generate secret key use secret_key_generator.py

```
python secret_key_generator.py
```

Set RAVEN_DSN to anything. Integration with Sentry is not important in development environment

- do standard django initialization

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Deployment using nginx + daphne is not tested yet