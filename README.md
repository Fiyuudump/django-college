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
