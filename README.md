## How to run
```sh
# install package requirement
$ pip install -r requirements.txt

# set permission in powershell for current session
$ Set-ExecutionPolicy Unrestricted -Scope Process

# set permission in powershell for current user
$ Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# activate virtual environment
$ .\myenv\Scripts\activate

# activate using bash
$ source myenv/Scripts/activate

# project creations
$ django-admin startproject <project_name>

# app inside project creations
$ py manage.py startapp <app_name>

# models creations
$ py manage.py migrate
$ py manage.py makemigrations
$ py manage.py runserver

# super user creations
$ py manage.py createsuperuser

```

## Setup Project for Deploy on phytonanywhere.com (Django, SQLite)
1. setup the pythonanywhere's Consoles and Files (`package`, `virtual env`, `project's python files`)
- clone the repository
- make virtual environment
  ```bash
  mkvirtualenv <your_venv> # example: mkvirtualenv myenv
  ```
- install requirements.txt
  ```bash
  # ! make sure you are in `requirements.txt` directory path
  pip install -r requirements.txt
  ```
- setup and manage pythonanywhere's staticfiles
  ```python
  # at your ../your_project/settings.py
  ...

  ALLOWED_HOSTS = ['*']

  CSRF_TRUSTED_ORIGINS = [
    "https://*.free.pinggy.link",
    "https://*.trycloudflare.com",
    "https://*.pythonanywhere.com",
  ]

  ...
  ...

  import os
  STATIC_URL = '/static/' # update the value from 'static/' to '/static/'
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # add this line
  STATICFILES_URL = [
    os.path.join(BASE_DIR, 'static')
  ]
  ```
  and run this command on bash :
  ```bash
  # at your ../your_project/settings.py
  python manage.py collectstatic
  ```


  If you got error template not found for structure folder like below, please add this some configuration :
  ```bash
  /home/yourusername/galang-porto/
  ├── manage.py
  ├── galang_porto/
  │   ├── views.py
  │   ├── settings.py
  │   └── ...
  └── templates/
      └── index.html
  ```

  add this configuration please :
  ```python
  ...

  import os

  BASE_DIR_V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # add this line

  TEMPLATES = [
    {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [os.path.join(BASE_DIR_V2, 'templates')], # from 'DIRS': ['templates']
      # or using absolute path like below :
      # 'DIRS': ['/home/yourusername/galang-porto/templates']
      'APP_DIRS': True,
      'OPTIONS': { ... },
    },
  ]

  ...
  ```

  In your `views.py` file no need to adjust again:
  ```python
  ...

  def home(request):
    return render(request, 'index.html', context)

  ...
  ```

2 setup pythonanywhere's Web (`source code`, `WSGI configuration file`, `Virtualenv`, `Static files`)
- setup the source code

  copy absolute path, and paste into pythonanywhere's source code input. example: `/home/tyo/django-college/blog`
- setup the WSGI configuration file

  click on the pythonanywhere's WSGI configuration file, which is hyperlink `/var/www/tyo_pythonanywhere_com_wsgi.py`, and edit the `DJANGO` section into these sake of line code:
  ```python
  ...

  # +++++++++++ DJANGO +++++++++++
  # To use your own django app use code like this:
  import os
  import sys

  # assuming your django settings file is at '/home/tyo/mysite/mysite/settings.py'
  # and your manage.py is is at '/home/tyo/mysite/manage.py'
  path = '/home/tyo/django-college/blog' # the path of your source code
  if path not in sys.path:
    sys.path.append(path)

  os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings' # the path of your settings.py file configuration

  # then:
  from django.core.wsgi import get_wsgi_application
  application = get_wsgi_application()

  ...

  ```
- setup the Virtualenv

  copy only the virtualenv name and paste it into pythonanywhere's virtual env. example: `myenv`
- PythonAnywhere static mapping

  setup the pythonanywhere's static file into input section. example:
  ```txt
  URL: <your_static_url>   →   Directory: <your_absolute_staticfiles_folder>

  # to

  URL: /static/   →   Directory: /home/tyo/django-college/blog/staticfiles
  ```
  and if the css not included by `$ python manage.py collectstatic`'s command before, add the raw `static` folder absolute path. example :
  ```txt
  URL: <your_static_url>   →   Directory: <your_absolute_raw_static_folder>

  # to

  URL: /static/   →   Directory: /home/tyo/django-college/blog/static
  ```
