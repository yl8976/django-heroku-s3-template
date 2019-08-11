# Django Heroku S3 Template

Template for websites built using Django and deployed on Heroku and AWS S3.

## Requirements

- `Django` (2.2.4)
- `Python` (3.7.3)
- `PostgreSQL` (11)

## Setup
### Renaming the Django Project
[Source](https://www.techinfected.net/2016/08/how-to-change-your-django-project-name.html)

If you would like to rename your Django project after you've created it (I often end up doing this because I want to name my app the project name, not the project itself), this is the way to do it.
Your current Django project structure should look like this:

```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
Rename your project directory (myproject) and the following inside your project directory:
ROOT_URLCONF = 'NewProjectName.urls'
WSGI_APPLICATION = 'NewProjectName.wsgi.application'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewProjectName.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewProjectName.settings')
There is no need to make any changes to any of your apps.
