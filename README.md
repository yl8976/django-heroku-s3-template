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
│   │       └── model_form_upload.html
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

Rename your project directory (`myproject`) and the following files inside your project directory into your own project name (the examples below use `newprojectname` as the new name):

```python
# myproject/settings.py
ROOT_URLCONF = 'newprojectname.urls'
WSGI_APPLICATION = 'newprojectname.wsgi.application'
```

```python
# myproject/wsgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newprojectname.settings')
```

```python
# manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newprojectname.settings')
```

```text
# Procfile
web: gunicorn newprojectname.wsgi --log-file -
```

Lastly, rename the root folder `django-heroku-s3-template` to whatever you want to call your project. It's common to just name it the same name as your project, although it does not affect your Django app in any way.

### Rename the Django App

This template also comes with a barebones Django app called `myapp`. It contains some templates for uploading files, a model describing a Django form, and views that handle the appropriate requests. Rename these to an appropriate app name in the following files (the examples below use `newappname` as the new name):

```python
# myproject/urls.py
"""newappname URL Configuration
```

```python
# myproject/urls.py
from newappname import views
```

```python
# myproject/settings.py
INSTALLED_APPS = [
    'newappname.apps.NewappnameConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
]
```

```python
# myproject/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'newappname_db',
        'USER': 'newappnameuser',
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

```python
# myapp/views.py
return render(request, 'newappname/home.html', { 'documents': documents })
```

```python
# myapp/views.py
return render(request, 'newappname/model_form_upload.html', {
        'form': form
    })
```

```python
# myapp/apps.py
class NewappnameConfig(AppConfig):
    name = 'newappname'
```

```html
<!-- myapp/templates/myapp/home.html -->
{% extends 'newappname/base.html' %}
```

```html
<!-- myapp/templates/myapp/model_form_upload.html -->
{% extends 'newappname/base.html' %}
```

Don't forget to rename the folders `myapp` and `myapp/templates/myapp` as well!

### Installing Dependencies

In the command line, navigate to the project's root folder and run

```bash
python3 -m venv env
```

This will create a virtual environment called `env` (using Python 3's native virtual environment module, `venv`) where we can install our dependencies separately from other Python projects. Now run

```bash
source env/bin/activate
pip install -r requirements.txt
```

to install our dependencies.

### Using `python-dotenv` for Local Development

This package allows you to load variables into our Django project as environment variables so that it will stay out of source control. This is particularly important for Django projects in two places: the `SECRET_KEY` in `settings.py`, our AWS keys, and our database's password, also stored in `settings.py`.

The way it works is simple: we just create a file `.env` within our project (which will store our sensitive data), and now we'll be able to import it anywhere within the project and load our environment variables. We just have to make sure **not** to add `.env` to source control!
To begin, create an empty `.env` file in the same folder where our `settings.py` is using the `touch` command:

```bash
cd myproject # If you're not already in the folder
touch .env
```

To recap, our folder structure should now look like this (but your project and app will have been renamed):

```text
django-heroku-s3-template
├── .env <- note this new file!
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
│   │       └── model_form_upload.html
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

This template already has the following code added to the top of `settings.py` to load our `.env` file:

```python
from dotenv import load_dotenv
load_dotenv()
```

At this point, parsed key-value pairs from the `.env` file is now present as system environment variables and they can be conveniently accessed via the method `os.getenv()`. Generate a `SECRET_KEY` value using [this generator](https://www.miniwebtool.com/django-secret-key-generator/) and copy the value of `SECRET_KEY` in `settings.py` and add it to `.env` like so, along with your PostgreSQL database password and AWS Keys:

```text
SECRET_KEY=YOURSECRETKEY
DB_PASSWORD=YOURDBPASSWORD
AWS_ACCESS_KEY_ID=YOURAWSACCESSKEYID
AWS_SECRET_ACCESS_KEY=YOURAWSSECRETACCESSKEY
S3_BUCKET=NAMEOFYOURAWSS3BUCKET
```

Note how there are **no spaces** around the equal signs and there are **no quotation marks** for the variable values. When you deploy to Heroku, you'll define them in the Config Vars section in the project's Settings tab instead.

And that's it! Hopefully this template comes in handy for some people building Django apps like myself.

### Additional Resources
- [Heroku: Using AWS S3 to Store Static Assets and File Uploads](https://devcenter.heroku.com/articles/s3)
- [Medium: Setting up Amazon S3 Bucket for serving Django Static and Media files](https://medium.com/@manibatra23/setting-up-amazon-s3-bucket-for-serving-django-static-and-media-files-3e781ab325d5)
- [Simple is Better Than Complex: How to Upload Files With Django](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html) (note: this template's model and form is based off of this tutorial)
