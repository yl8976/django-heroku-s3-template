# Django Heroku S3 Template

Template for websites built using Django and deployed on Heroku and AWS S3.

## Requirements

- `Django` (2.2.4)
- `Python` (3.7.3)
- `PostgreSQL` (11)

## Setup

### Clone the Template

First, navigate to the folder you want your project to live on your command line interface (`cmd.exe` on Windows, `Terminal` on macOS). Then, type:

```bash
git clone https://github.com/younglee327/django-heroku-s3-template.git
```

### Rename the Django Project

[Source](https://www.techinfected.net/2016/08/how-to-change-your-django-project-name.html)

If you would like to rename your Django project after you've created it (I often end up doing this because I want to name my **app** the project name, not the project itself), this is the way to do it.
Your current Django project structure should look like this:

```text
django-heroku-s3-template
├── Procfile
├── README.md
├── manage.py
├── myapp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates
│   │   └── myapp
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── model_form_upload.html
│   │       └── simple_upload.html
│   ├── tests.py
│   └── views.py
├── myproject
│   ├── __init__.py
│   ├── settings.py
│   ├── storage_backends.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── runtime.txt
```

Rename your project directory (`myproject`) and the following files inside your project directory into your own project name (the examples below use `NewProjectName` as the new name):

```python
# myproject/settings.py
ROOT_URLCONF = 'NewProjectName.urls'
WSGI_APPLICATION = 'NewProjectName.wsgi.application'
```

```python
# myproject/swsgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewProjectName.settings')
```

```python
# manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewProjectName.settings')
```

Lastly, rename the root folder `django-heroku-s3-template` to whatever you want to call your project. It's common to just name it the same name as your project, although it does not affect your Django app in any way.

### Rename the Django App

This template also comes with a barebones Django app called `myapp`. It contains some templates for uploading files, a model describing a Django form, and views that handle the appropriate requests.
