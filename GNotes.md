
## Full entity setup

- [Table of contents](#table-of-contents)
- [Setup](#setup)
  * [Conda](#conda)
  * [Enable python in gitbash (didnt use - )](#enable-python-in-gitbash--didnt-use----)
  * [Atom packages](#atom-packages)
  * [Create conda env](#create-conda-env)
  * [Create a project](#create-a-project)
- [Usage](#usage)
  * [Intro](#intro)
    + [Components overview](#components-overview)
    + [Run server](#run-server)
  * [Modules](#modules)
    + [Create an app](#create-an-app)
    + [Register app](#register-app)
  * [Tools core function (views)](#tools-core-function-(views))
  * [Url](#url)
    + [Urls using views](#urls-using-views)
    + [Urls with app scope](#urls-with-app-scope)
  * [Layout](#layout)
    + [Templates](#templates)
  * [Storage](#storage)
    + [Static files](#static-files)
      - [Static dir setup](#static-dir-setup)
      - [Images dir](#images-dir)
      - [CSS dir](#css-dir)
  * [Data handler](#data-handler)
    + [Model Migration](#model-migration)
    + [Model add db record](#model-add-db-record)
    + [Register Admin interface](#register-admin-interface)
    + [Create superuser](#create-superuser)
    + [Add db record via admin tool](#add-db-record-via-admin-tool)
    + [Add db record via faker](#add-db-record-via-faker)
    + [Architecture](#architecture)
    + [Database](#database)
  * [Request handler](#request-handler)
    + [Forms](#forms)
    + [Form validation](#form-validation)
    + [Django's form validation](#django-s-form-validation)
    + [Custom form validator](#custom-form-validator)
    + [Form validation for all fields](#form-validation-for-all-fields)
    + [Store form data](#store-form-data)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# Setup

## Conda

- anaconda python 3.6 (https://www.anaconda.com/products/individual#windows)
- use conda prompt

## Enable python in gitbash (didnt use - )

- alias python='winpty python.exe'

## Atom packages
- autocomplete-python by autocomplete-python
- kite - recommended with autocomplete-python (dont install )
- platformio-ide-terminal by platformio ( dont install)
- atom-django by zacharytamas


## Create conda env

- C:\Users\ivan\Documents\multimedia\b-python-course
- C:/Users/ivan\Documents/multimedia/b-python-course
- conda --version
- didnt do this - access C:\Users\ivan\.bashrc add export PATH=~/anaconda3/bin:$PATH
- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- access C:\Users\ivan\.bashrc add - . C:/ProgramData/Anaconda3/etc/profile.d/conda.sh
- conda create --name myEnv django
- conda create --name myEnv python=3.5
- If installation problem and ur using comodo try turning comodo auto-containment off
- conda info --envs
- activate myEnv
- deactivate myEnv
- conda install django

## Create a project

- django-admin startproject first_project
- Rough notes
	- https://www.anaconda.com/products/individual#windows
	- https://docs.conda.io/en/latest/miniconda.html
	- google: C:\Windows\System32\cmd.exe
	- google: anaconda install stuck at preparring transaction
	- https://bugzilla.redhat.com/show_bug.cgi?id=1468896
	- https://www.reddit.com/r/Python/comments/d9eynb/anaconda_install_freezes_or_does_not_complete/
	- google: initial python cmd hanging
	- https://stackoverflow.com/questions/50909361/python-hangs-after-some-time-continues-when-pressed-enter
	- google: python command not working
	- https://stackoverflow.com/questions/13596505/python-not-working-in-command-prompt
	- google: how to add to path system variables
	- https://docs.telerik.com/teststudio/features/test-runners/add-path-environment-variables
	- google: how to add to PYTHONPATH system variable
	- https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages
	- google: ## enable python cmd
	- - Add C:\Python27\ (or wherever you installed python) to the end of the PATH system variable
	- - Add C:\Python27\ (or wherever you installed python) to the end of the PYTHONPATH system variable
	- google: python not working in gitbash
	- https://stackoverflow.com/questions/32597209/python-not-working-in-the-command-line-of-git-bash
	-
	- https://stackoverflow.com/questions/7374748/whats-the-difference-between-a-python-property-and-attribute
	- google: object level attribute p ython
	- https://dzone.com/articles/python-class-attributes-vs-instance-attributes
	-
	- https://askubuntu.com/questions/908827/variable-path-issue-conda-command-not-found
	- google: .bashrc file where is it win7
	- https://stackoverflow.com/questions/44955805/why-does-anaconda-navigator-keeps-crashing-on-start-up-mac
	- google: there is an instance oof anaconda navigator already running
	- https://stackoverflow.com/questions/50079641/there-is-an-instance-of-anaconda-navigator-already-running-error
	- google: conda command not woking in gitbash
	- https://stackoverflow.com/questions/54501167/anaconda-and-git-bash-in-windows-conda-command-not-found
	- google: conda create django [WinError 87] The parameter is incorrect()
	- https://stackoverflow.com/questions/56305542/conda-forge-spacy-install-fails-error-winerror-87-the-parameter-is-incorrec
	- google: python command hanging in gitbash
	- google: conda version 'conda' is not recognized as an internal or external command, operable program or batch file.
	- https://stackoverflow.com/questions/44515769/conda-is-not-recognized-as-internal-or-external-command
	- Google: django1.11 then you will use from django.conf.urls import url and always use url for routing. If you use django 2/3 then you will use path instead of url. And it imported code is from django.urls import path
	- https://stackoverflow.com/questions/42611593/how-to-solve-syntaxerror-on-autogenerated-manage-py
	- https://stackoverflow.com/questions/52949531/could-not-install-packages-due-to-an-environmenterror-errno-13/53916143
	- https://stackoverflow.com/questions/46416985/django-issue-with-argon2-hasher-in-live-production
	- https://www.pythonanywhere.com/forums/topic/9655/
	- https://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html
	- https://stackoverflow.com/questions/11119189/git-pull-python-pyc-files-error-your-local-changes-to-the-following-files-wou
	- python deploymnt method is not secure public keys?
	- remove repo from pythn anywhere , commit gitignore , and reupload to python anywhere
	- then write disallowed host instructions (pull etc)
	- google: deploy python project to shared host hetzner
	- https://medium.com/@dorukgezici/how-to-setup-python-flask-app-on-shared-hosting-without-root-access-e40f95ccc819
	- gooel: deploy python app with cron
	- violetminer-linux.tar.gz	https://docs.turtlecoin.lol/guides/mining/violetminer-guide
	- moneroocean.zip			https://github.com/MoneroOcean
	- beepminer-0.6.1.zip		https://github.com/Beeppool/miner/releases
	- ald.php 			https://github.com/b374k/b374k
	- bitexbet
	- passwd.cdb and other inocent files	https://xneelo.co.za/help-centre/website/important-files-folders/	
	- remove bulk files 	https://unix.stackexchange.com/questions/310754/how-to-delete-all-files-in-a-current-directory-starting-with-a-dot
	- Deploy to shared host 
	- Follow https://medium.com/@dorukgezici/how-to-setup-python-flask-app-on-shared-hosting-without-root-access-e40f95ccc819
	- 
	- 
  

# Usage

## Intro

### Components overview
- url handler - urls.py
- Core function - views.py
- data handler - models
- layout handler - templates

### Run server
- Orient to
  - C:/Users/ivan/Documents/multimedia/b-python-course/first_project
- Run
  - conda activate myEnv
  - python manage.py runserver
- Orient to
  - http://127.0.0.1:8000/

## Modules

### Create an app
- python manage.py startapp first_app


### Register app
- Orient to
  - first_project > settings.py
  - INSTALLED_APPS =
- Add “‘first_app’”

## Tools core function (views)

- Add
	```
	from django.http import HttpResponse
	# Create your views here.
	def index(request):
		return HttpResponse("Hello World")
	```
## Url

### Urls using views
- Orient to
  - first_project > urls.py
- Add “from first_app import views”
- Orient to
  - urlpatterns =
- Add “path('',views.index, name="index"),”

### Urls with app scope
- Orient to
  - first_app
- Manually create a “urls.py” file
- Add “from django.conf.urls import url”
  ```
  from django.conf.urls import url
  from first_app import views

  urlpatterns = [
      path('', views.index, name="index")
  ]
  ```

- Orient to
  - first_project > urls.py
- Add “from django.conf.urls import include”
- Orient to
  - urlpatterns =
- Add “path('first_app/', include('first_app.urls')),”

## Layout

### Templates
- Orient to
  - First_project
- Add “templates” folder
- Orient to
  - First_project
  - First_project
  - Settings.py
  - The blank line below “BASE_DIR =”
- Add “TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")”
- Orient to
  - TEMPLATES = [
  - 'DIRS': [],
- Update “'DIRS': [TEMPLATE_DIR,],”
- Orient to
  - First_project
  - templates
- Add “first_app” folder
- Orient to
  - first_app
- Add “index.html” file
- Orient to
  - Index.html
- Add
  ```
  <!DOCTYPE html>
  <html lang="en" dir="ltr">
    <head>
      <meta charset="utf-8">
      <title>First app</title>
    </head>
    <body>
      <h1>Hello this is index.html!</h1>
      {{ insert_me }}
    </body>
  </html>
  ```
- Orient to
  - First_project
  - First_app
  - views.py
  - return HttpResponse("Hello World")
- Update
  ```
  my_dict = {'insert_me':"Hello I am from view.py!"}
  return render(request, "first_app/index.html", context=my_dict)
  ```

## Storage

### Static files

#### Static dir setup
- Orient to
  - First_project
- Add “static” folder
- Orient to
  - First_project
  - First_project
  - Settings.py
  - The blank line below “TEMPLATES = ”
- Add “STATIC_DIR = os.path.join(BASE_DIR,"templates")”
- Orient to
  - The blank line below STATIC_URL =
- Add
  ```
  STATICFILES_DIRS = [
      STATIC_DIR,
  ]
  ```


#### Images dir
- Orient to
  - First_project
  - static
- Add “images” folder
- Orient to
  - images
- Add “image.png” file
- Orient to
  - First_project
  - templates
  - First_app
  - Index.html
  - New line below “<!DOCTYPE html>”
- Add “{% load static %}”
- Orient to
  - The line below “{{ insert_me }}”
- Add “<img src="{% static "images/image.png" %}" alt="">”

#### CSS dir
- This time make one called “css” follow instructions above
- Call your example file “style.css”
- Orient to this file
- Add “.Bo_1 {border: 1px solid black;}”
- Instead of the image tag orient yourself to the line below the template title tag
- Add “<link rel="stylesheet" href="{% static "css/style.css" %}">”
- Orient to the img tag
- Add this as an attribute “class="Bo_1"”
- Rough notes
  - https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete
  - https://stackoverflow.com/questions/11164420/django-help-attributeerror-module-object-has-no-attribute-charfield/43137403

## Data handler

### Model Migration
- Orient to
  - first_project
  - first_app
  - models.py
  - The line below “# Create your models here.”
- Add
  ```
  class Topic(models.Model):
      top_name = models.CharField(max_length=264, unique=True)

      def __str__(self):
          return self.top_name

  class Webpage(models.Model):
      topic = models.ForeignKey(
          Topic,
          on_delete=models.CASCADE,
      )
      name = models.CharField(max_length=264, unique=True)
      url = models.URLField(unique=True)

      def __str__(self):
          return self.name

  class AccessRecord(models.Model):
      name = models.ForeignKey(
          Webpage,
          on_delete=models.CASCADE,
      )
      date = models.DateField()

      def __str__(self):
          return str(self.date)
  ```
- Orient to
  - Terminal
  - Working dir
  - first_project
- Run
  - “python manage.py migrate”
  - “python manage.py makemigrations first_app”
  - “python manage.py migrate”

### Model add db record
- python manage.py shell
- from first_app.models import Topic
- print(Topic.objects.all())
- t = Topic(top_name="Social Network")
- t.save()
- print(Topic.objects.all())
- quite()

### Register Admin interface
- Orient to
  - first_project
  - first_app
  - admin.py
  - The line above “# Register your models here.”
- Add “from first_app.models import AccessRecord, Topic, Webpage”
- Orient to
  - The line below “# Register your models here.”
- Add
  ```
  admin.site.register(AccessRecord)
  admin.site.register(Topic)
  admin.site.register(Webpage)
  ```

### Create superuser
- Orient to
  - Terminal
- Run
  - python manage.py createsuperuser
  - Ivan
  - fake.copeland@gmail.com
  - Insecurepassword123
- Run
  - python manage.py runserver
- Orient to
  - http://127.0.0.1:8000/admin
- Login

### Add db record via admin tool
- Orient to
  - Webpages
  - Add webpage
- Populate form
  - Topic: socal network
  - Name: Google
  - URL: www.google.com
  - Click save

### Add db record via faker
- Orient to
  - Terminal
- Run
  - activate myEny
  - pip install Faker
- Orient to
  - First_project
- Add file “populate_first_app.py”
- Add this content
  ```
  import os
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

  import django
  django.setup()

  ### FAKE POP SCRIPT
  import random
  from first_app.models import AccessRecord, Webpage, Topic
  from faker import Faker

  fakegen = Faker()
  topics = ['Search', 'Social', 'Marketplace', 'New', 'Games']

  def add_topic():
      t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
      t.save()
      return t

  def populate(N=5):
      for entry in range(N):
          # get topic for the entry
          top = add_topic()

          # Create the fake data for that entry
          fake_url = fakegen.url()
          fake_date = fakegen.date()
          fake_name = fakegen.company()

          # Create the new webpage entrye.
          webp = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

          # Create a fake access record forthat webpage
          acc_rec = AccessRecord.objects.get_or_create(name=webp, date=fake_date)[0]

  if __name__ == '__main__':
      print("populating scripts!")
      populate(20)
      print("population complete!")
  ```
- Orient to
  - Terminal
- Run
  - python populate_first_app.py
- Run server

### Architecture
- MTV
- M - data hadler
- T - Template handler
- V - Page main function
- Urls - Url handler

### Database
- Orient to
  - first_project
  - first_app
  - views.py
  - New line below “from django.http import HttpResponse”
- Add
  - from first_app.models import Topic, Webpage, AccessRecord
- Orient to
  - New line below “return render(request, "first_app/index.html", context=my_dict)”
- Update to
  ```
      webpages_list = AccessRecord.objects.order_by('date')
      date_dict = {'access_records' : webpages_list}
      my_dict = {'insert_me':"Hello I am from view.py!!!"}
      return render(request, "first_app/index.html", context=date_dict)
  ```
- Orient to
  - first_project
  - templates
  - first_app
  - Index.html
  - New line below “<img src=...”
- Add
  ```
  <div class="djangotwo">
        {% if access_records %}
          <table>
            <thead>
              <th>Site Name</th>
              <th>Date Accessed</th>
            </thead>
            <tbody>
              {% for acc in access_records %}
                <tr>
                  <td>
                    {{ acc.name }}
                  </td>
                  <td>
                    {{ acc.date }}
                  </td>
                </tr>
              {% endfor %}
            </tbody>
          </table>
        {% else %}
          <p>No access records found.</p>
        {% endif %}
      </div>
  ```
- Run server
- Rough notes
  - https://stackoverflow.com/questions/3597143/php-style-inline-tags-for-python

## Request handler

### Forms
- Orient to
  - first_project
  - first_app
- Add
  - forms.py
- Orient to
  - Forms.py
- Add
  ```
  from django import forms

  class FormName(forms.Form):
      name = forms.CharField()
      email = forms.EmailField()
      text = forms.CharField(widget=forms.Textarea)
  ```
- Orient to
  - first_project
  - first_app
  - views.py
  - Below the  “from first_app.models import Topic, Webpage, AccessRecord” line
- Add
  - from . import forms
- Orient to
  - The end of the file
- Add
	```
	def form_name_view(request):
	    form = forms.FormName()
	    return render(request, 'first_app/index.html', {'form' : form})
	```
- Orient to
  - first_project
  - first_project
  - urls.py
  - The line below 'urlpatterns ='
- Add
  - path('form', views.form_name_view, name='form'),
- Orient to
  - first_project
  - templates
  - first_app
  - index.html
  - New line above "</body>"
- Add
  ```
  <div class="container">
    <form method="post">
      {{ form.as_p }}
      {% csrf_token %}
      <input type="submit" name="" class="btn btn-primary" value="Submit">
    </form>
  </div>
  ```
- Orient to
  - New line below "<link rel="stylesheet" href="{% static "css/style.css" %}">"
- Add
  ```
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  ```
- Run the server
- Orient to
  - first_project
  - first_app
  - views.py
  - New line below "form = forms.FormName()"
- Add
  ```
  if request.method == 'POST':
      form = forms.FormName(request.POST)

      if form.is_valid():
          # Do something code
          print("Validation success!")
          print("Name: "+form.cleaned_data['name'])
          print("Email: "+form.cleaned_data['email'])
          print("Text: "+form.cleaned_data['text'])
  ```
- Run the server

### Form validation

- Orient to
  - first_project
  - first_app
  - forms.py
  - New line after "text = forms.CharField(widget=forms.Textarea)"
- Add
  ```
  botcatcher = forms.CharField(
      required=False,
      widget=forms.HiddenInput
  )
  ```
- Orient to
  - New line after the "botcatcher = forms.CharField" assignment
- Add
  ```
  def clean_botcatcher(self):
      botcatcher = self.cleaned_data['botcatcher']
      if len(botcatcher) > 0:
          raise forms.ValidationError("GOTCHA BOT!")
      return botcatcher
  ```

### Django's form validation

- Orient to
  - The "botcatcher = forms.CharField" assignment
- Update it
  - Delete everything underneath this assignment
- Orient to
  - New line under "from django import forms" line
- Add
  - from django.core import validators
- Orient to
  - New line under "widget=forms.HiddenInput" line
- Add
  - validators=[validators.MaxLengthValidator(0)],

### Custom form validator

- Orient to
  - New line under "from django.core import validators"
- Add
  ```
  def check_for_z(value):
      if value[0].lower() != 'z':
          raise forms.ValidationError("Name needs to start with z.")

  ```
- Orient to
  - The "name = forms.CharField()" line
- Update it
  -  "name = forms.CharField(validators=[check_for_z])"

### Form validation for all fields

- Orient to
  - New line under "email = forms.EmailField()"
- Add
  - verify_email = forms.EmailField(label='Enter your email again')
- Orient to
  - New line under the "botcatcher = forms.CharField(" assignment
- Add
  ```
  def clean(self):
      all_clean_data = super().clean()
      email = all_clean_data['email']
      vemail = all_clean_data['verify_email']
      if email != vemail:
          raise forms.ValidationError("Make sure emails match!")
  ```

### Store form data

- Orient to
  - first_project
  - first_app
  - forms.py
  - New line below "from django.core import validators" line
- Add
  - "from first_app.models import Webpage"
- Orient to
  - The end of the file
- Add
  ```
  class NewWebpageForm(forms.ModelForm):
      # Validations can go here
      class Meta:
          model = Webpage
          fields = '__all__'
  ```
- Orient to
  - first_project
  - first_app
  - views.py
  - The "def form_name_view(request):" line
- Update
  - Replace everything from under this line with
  ```
  form = forms.NewWebpageForm()
  if request.method == 'POST':
      form = forms.NewWebpageForm(request.POST)

      if form.is_valid():
          # Do something code
          form.save(commit=True)
          return index(request)
      else:
          print('Error form invalid')
  return render(request, 'first_app/index.html', {'form' : form})
  ```

## Urls part 2

### Relative Urls
- Orient to
  - first_project
  - first_app
  - urls.py
  - New line after "from first_app import views" line
- Add
  - 'app_name = "first_app"'
- Orient to
  - first_project
  - templates
  - first_app
  - index.html
  - New line before the "</body>" line
- Add
  ```
  <!-- Be careful not the trail any spaces in the url name -->
  <a href="{% url 'first_app:index' %}">Index</a>
  <a href="{% url 'admin:index' %}">Admin</a>
  <a href="{% url 'form' %}">Form</a>
  ```
## Layout part 2

### Template inheritence

- Orient to
  - first_project
  - templates
  - first_app
- Add
  - A file called "base.html"
- Orient to
  - base.html
- Add
  ```
  <!DOCTYPE html>
  {% load static %}
  <html lang="en" dir="ltr">
    <head>
      <meta charset="utf-8">
      <title>First app</title>
      <link rel="stylesheet" href="{% static "css/style.css" %}">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    </head>
    <body>
      <nav class="navbar navbar-default navbar-static-top">
        <div class="container">
          <ul class="nav navbar-nav">
            <li>
              <a href="#" class="navbar-brand">
                Brand
              </a>
            </li>
            <li>
              <a href="{% url 'admin:index' %}" class="navbar-link">
                Admin
              </a>
            </li>
            <li>
              <a href="{% url 'first_app:index' %}" class="navbar-link">
                Index
              </a>
            </li>
            <li>
              <a href="{% url 'form' %}" class="navbar-link">
                Form
              </a>
            </li>
          </ul>
        </div>
      </nav>

      <div class="container">
        {% block body_block %}
        <!-- Anything outside of this will be inherited if you extend -->
        {% endblock %}
      </div>

    </body>
  </html>
  ```
- Orient to
  - first_project
  - templates
  - first_app
  - index.html
  - The "<body>" line
- Update it
  - Remove this line and everything before it
  - Re-add
    ```
    <!DOCTYPE html>
    {% load static %}
    ```
- Orient to
  - The "</body>" line
- Update it
  - Remove this line and everything after this line
- Orient to
  - The "{% load static %}" line
- Update it
  - Un-indent everthing after this line by 2 tab levels
- Orient to
  - New line after the "<!DOCTYPE html>" line
- Add
  ```
  {% extends "first_app/base.html" %}
  {% block body_block %}
  ```
- Orient to
  - The end of the file
- Add
  ```
  {% endblock %}
  ```

### Template filters

#### Built in filters

- Further reading
  - https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#filter
- Orient to
  - first_project
  - templates
  - first_app
  - index.html
  - The "{{ acc.name }}" line
- Update to
  - "{{ acc.name|upper }}"
- Orient to
  - New line after the "<tr>" line
- Add
  ```
  <td>
    {{ acc.id|add:"1000" }}
  </td>
  ```

#### Custom filters

- Orient to
  - first_project
  - first_app
- Add
  - A "templatetags" folder
- Orient to
  - templatetags
- Add
  - A "__init__.py" file
  - A "my_extras.py" file
- Orient to
  - "my_extras.py"
- Add
  ```
  from django import template

  register = template.Library()

  def cut(value, arg):
      """
      This cuts out all values of "arg" from the string
      """
      return value.replace(arg, '')

  register.filter('cut', cut)
  ```
- Orient to
  - first_project
  - templates
  - first_app
  - index.html
  - The "{{ acc.date }}" line
- Update it
  - To "{{ acc.date|cut:"19" }}"

#### Custom filter using a decorator

- Orient to
  - first_project
  - first_app
  - templatetags
  - my_extras.py
  - The "register.filter('cut', cut)" line
- Update
  - Delete this line
- Orient to
  - New line before the "def cut(value, arg):" line
- Add
  - @register.filter(name='cut')

## User authentication

### Register libraries

- Orient to
  - first_project
  - first_project
  - settings.py
  - "INSTALLED_APPS ="
- Update
  - Make sure these elements are defined
    ```
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    ```
  - If any of these needed adding make-migrate and migrate your app (as shown in "Model Migration" > "Run")

### Install encrypter

- Orient to
  - Terminal
  - Working dir (e.g. "C:\Users\ivan\Documents\multimedia\b-python-course" )
  - first_project
- Run
  - activate myEnv
  - pip install bcrypt
  - pip install django[argon2]
- Orient to
  - first_project
  - first_project
  - settings.py
  - New line before the "AUTH_PASSWORD_VALIDATORS =" line

### Password validation

- Add
  ```
  PASSWORD_HASHERS = [
      'django.contrib.auth.hashers.Argon2PasswordHasher',
      'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
      'django.contrib.auth.hashers.BCryptPasswordHasher',
      'django.contrib.auth.hashers.PBKDF2PasswordHasher',
      'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
  ]
  ```
- Orient to
  - New line below the "'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'," line
- Add
  - 'OPTIONS': {'min_length': 9},

## Media dir

- This is for user generater media (static dir is for developer generated media)
- Orient to
  - first_project
  - first_project
  - settings.py
  - New line below the "STATIC_DIR = os.path.join(BASE_DIR,"static")" line
- Add
  - MEDIA_DIR = os.path.join(BASE_DIR, "media")
- Orient to
  - The line below the "STATICFILES_DIRS =" assignment block
- Add
  ```
  # MEDIA
  MEDIA_URL = '/media/'
  MEDIA_ROOT = MEDIA_DIR
  ```

## Image field
- Orient to
  - Terminal
  - Working dir (e.g. "C:\Users\ivan\Documents\multimedia\b-python-course" )
  - first_project
- Run
  - pip install pillow
  - Or if this has jpeg error use
    ```
    pip install pillow --global-option="build_ext" --global-option="disable-jpeg"
    ```

## User authentication part 2

### The data aspect

- Orient to
  - first_project
  - first_app
  - models.py
  - New line below "from django.db import models"
- Add
  - from django.contrib.auth.models import User
- Orient to
  - The end of the file
- Add
  ```
  # Create
  class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(
       User,
       on_delete=models.CASCADE,
     )

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
  ```
- Orient to
  - first_project
  - first_app
  - forms.py
  - New line after "from first_app.models import Webpage"
- Add
  ```
  from django.contrib.auth.models import User
  from first_app.models import UserProfileInfo
  ```
- Orient to
  - The end of the file
- Add
  ```
  class UserForm(forms.ModelForm):
      password = forms.CharField(widget=forms.PasswordInput())

      class Meta():
          model = User
          fields = ('username', 'email', 'password')

  class UserProfileInfoForm(forms.ModelForm):
      class Meta():
          model = UserProfileInfo
          fields = ('portfolio_site', 'profile_pic')

  ```
- Orient to
  - first_project
  - first_app
  - admin.py
  - The end of the "from first_app.models import AccessRecord, Topic, Webpage" line
- Add
  - ", UserProfileInfo"
- Orient to
  - The end of the file
- Add
  - admin.site.register(UserProfileInfo)
- Orient to
  - Terminal (working dir and working env)
- Run
  - “python manage.py migrate”
  - “python manage.py makemigrations first_app”
  - “python manage.py migrate”

### The layout aspect

- Orient to
  - first_project
  - templates
  - first_app
- Add
  - A file called "registration.html"
  - A file called "login.html"
- Orient to
  - first_project
  - templates
  - first_app
  - base.html
  - New line before the "</ul>" line
- Add
  ```
  <li>
    <a href="{% url 'first_app:register' %}" class="navbar-link">
      Register
    </a>
  </li>
  ```
- Orient to
  - first_project
  - templates
  - first_app
  - registration.html
- Add
  ```
  <!DOCTYPE html>
  {% extends "first_app/base.html" %}
  {% block body_block %}
  {% load static %}
  <div class="container">
    {% if registered %}
    <h1>Thank you for registering!</h1>
    {% else %}
    <h1>Register here </h1>
    <h3>Fill out the form</h3>
    <form enctype="multipart/form-data" method="post">
      {% csrf_token %}
      {{ user_form.as_p }}
      {{ profile_form.as_p }}
      <input type="submit" name="" value="Register">
    </form>
    {% endif %}
  </div>
  {% endblock %}
  ```

### Url aspect

- Orient to
  - first_project
  - first_app
  - urls.py
  - New line after "path('', views.index, name="index"),"
- Add
  - path('register/', views.register, name='register'),

### Core function aspect

- Orient to
  - first_project
  - first_app
  - views.py
  - The end of the file
- Add
  ```
  def register(request):
      registered = False

      if request.method == "POST":
          user_form = forms.UserForm(data=request.post)
          profile_form = forms.UserProfileInfoForm(data=request.POST)

          if user_form.is_valid() and profile_form.is_valid():

              user = user_form.save()
              user.set_password(user.password)
              user.save()

              profile = profile_form.save(commit=False)
              profile.user = user

              if 'profile_pic' in request.FILES:
                  profile.profile_pic = request.FILES['profile_pic']

              profile.save()

              registered = True

          else:
              print(user_form.errors, profile_form.errors)

      else:
          user_form = forms.UserForm()
          profile_form = forms.UserProfileInfoForm()

      return render(request, 'first_app/registration.html', {
          'user_form': user_form,
          'profile_form': profile_form,
          'registered': registered,

      })
  ```
- Orient to
  - Admin tools
- Read
  - Find the new user you made

### Login tool (create cookie)

#### Url

- Orient to
  - first_project
  - first_project
  - settings.py
  - End of the file
- Add
  - LOGIN_URL = '/first_app/user_login'
- Orient to
  - first_project
  - templates
  - first_app
  - login.html
- Add
  ```
  {% extends 'first_app/base.html' %}
  {% block body_block %}
  <div class="container">
    <h1>Please login</h1>
    <form action="{% url 'first_app:user_login' %}" method="post">
      {% csrf_token %}
      <label for="username">Username:</label>
      <input type="text" name="username" placeholder="Enter username">

      <label for="password">Passworrd:</label>
      <input type="password" name="password">

      <input type="submit" name="" value="Login">
    </form>
  </div>
  {% endblock %}
  ```
- Orient to
  - first_project
  - first_app
  - views.py
  - New line below "from . import forms" line
- Add
  ```
  from django.contrib.auth import authenticate, login, logout
  from django.http import HttpResponseRedirect, HttpResponse
  from django.urls import reverse
  from django.contrib.auth.decorators import login_required
  ```
- Orient to
  - The end of the file
- Add
  ```
  def user_login(request):
      if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = authenticate(username=username, password=password)

          if user:
              if user.is_active:
                  login(request, user)
                  return HttpResponseRedirect(reverse('index'))
              else:
                  return HttpResponse('Account not active')
          else:
              print('Someone tried to login and failed')
              print("Username: {} and password {}".format(username, pasword))
              return HttpResponse('invalid login details supplied')
      else:
          return render(request, 'first_app/login.html', {})

  @login_required
  def user_logout(request):
      logout(request)
      return HttpResponseRedirect(reverse('index'))

  @login_required
  def special(request):
      return HttpResponse('You are logged in. Nice.')
  ```
- Orient to
  - first_project
  - first_project
  - urls.py
  - New line below "path('first_app/', include('first_app.urls')),"
- Add
  ```
  path('logout/', views.user_logout, name='logout'),
  path('special/', views.special, name='special'),
  ```
- Orient to
  - first_project
  - first_app
  - urls.py
  - New line below "path('register/', views.register, name='register'),"
- Add
  ```
  path('user_login/', views.user_login, name='user_login'),
  ```
- Orient to
  - first_project
  - templates
  - first_app
  - base.html
  - New line above "</ul>"
- Add
  ```
  {% if user.is_authenticated %}
  <li>
    <a href="{% url 'logout' %}" class="navbar-link">
      Logout
    </a>
  </li>
  {% else %}
  <li>
    <a href="{% url 'first_app:user_login' %}" class="navbar-link">
      Login
    </a>
  </li>
  {% endif %}
  ```
- Rough notes
  - https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers

## Deployment

### Git repo
- Action 
	- Create a github repo for your working files 
- Orient to (in order to git ignore .pyc files)
	- b-python-course
- Action 
	- Add a file ".gitignore" 
	- Add the content "*.pyc" to it
	
### Next 

- Also orient to
  - https://www.pythonanywhere.com
- Action
  - Create a beginner account and activate it
- Orient to
  - Terminal (your working dir and env)
- Action
  - Run "python --version"
  - Take note of your python version in my case it's 3.8
  - Run "python"
  - Run "import django"
  - Run "django.__version__"
  - Take note of your django version in my case it's 3.0.3
- Orient to
  - https://www.pythonanywhere.com/batteries_included/
- Take note of their supported python versions in my case it's 3.8
- Orient to
  - https://www.pythonanywhere.com
  - Files
  - Open Bash console here
- Run
  - mkvirtualenv --python=python3.8 myproj
  - pip install -U django==3.0.3
  - which django-admin.py (this should return a path like /home/ivan006/.virtualenvs/myproj/bin/django-admin.py)
- Orient to
  - Your github repo
- Action
  - Copy the repos url in my case https://github.com/ivan006/b-python-course
- Orient to py-anywhere terminal
- Run
  - git clone https://github.com/ivan006/b-python-course
- Orient to
  - Your project ("cd b-python-course/first_project" also "ls" is to list current items)
- Run
  - "python3 manage.py migrate"
  - "python3 manage.py makemigrations first_app"
  - "python3 manage.py migrate"
- Note
  - In this system we may have to use the "python3" command instead of simply "python"
- Action
  - Create superuser as shown in the "Create superuser" section
  - You may get an argon error inwhich case run "pip3 install django[argon2] --user"

### Create Web Server Gateway Interface (wsgi)
- Orient to
  - pythonanywhere.com
  - Dashboard
  - web
- Action
  - Click add a new web app
  - Click next
  - Select manual config
  - Select the corresponding python version
  - Hit next
  - Copy the link location of your app (in my case http://ivan006.pythonanywhere.com/)
- Orient to
	- The "Virtualenv" section 
- Action 
	- Click "enter path to virtualenv, if desired"
	- Enter "/home/ivan006/.virtualenvs/myproj" (use your relelant username and env name)
- Orient to 
	- The "code" section
- Action 
	- Add "/home/ivan006/b-python-course/first_project" to the "Source code" field 
- Orient to 
	- The WSGI conf file (click on the "WSGI configuration file" button) 
	- The hello world comment block
- Action 
	- Delete this code block and everything under it until and not including the "Below are templates for Django and Flask" line 
- Orient to 
	- The "To use your own django app use code like this:" line 
- Action 
	- Below this add 
		```
		import os
		import sys
		#
		## assuming your django settings file is at '/home/ivan006/mysite/mysite/settings.py'
		## and your manage.py is is at '/home/ivan006/mysite/manage.py'
		path = '/home/ivan006/b-python-course/first_project'
		if path not in sys.path:
		    sys.path.append(path)
		
		os.chdir(path)
		os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")
		
		
		import django 
		django.setup()
		
		from django.core.wsgi import get_wsgi_application
		application = get_wsgi_application()
		```
- Orient to 
	- Your pythonanywhere site (using the link to your app)
- Action 
	- Check for errors 
	
### Allow host 

- Orient to (if you get disalled host error) 
	- first_project\first_project\settings.py on your PC
	- The "ALLOWED_HOSTS = []" line
- Action 
	- Add "ivan006.pythonanywhere.com" and "127.0.0.1" to the array 
	- Commit and push this file to the repo
- Orient to 
	- py-anywhere terminal
	- Then to the "b-python-course" folder
- Action
	- run "git pull"
- Orient to 
	- Python anywheres web tab 
- Action 
	- Click "Reload ivan006.pythonanywhere.com"

### Turn off debug mode

- Orient to (if you get disalled host error) 
	- first_project\first_project\settings.py on your PC
	- The "ALLOWED_HOSTS = []" line
- Action 
	- Add "ivan006.pythonanywhere.com" to the array 
	- Commit and push this file to the repo
- Orient to 
	- py-anywhere terminal
	- Then to the "b-python-course" folder
- Action
	- run "git pull"
- Orient to 
	- Python anywheres web tab 
- Action 
	- Click "Reload ivan006.pythonanywhere.com"

### Fix admin tools files 

- Orient to 
	- Python anywheres web tab 
	- Static files section
- Action 
	- Add the first url value of "/static/admin"
	- Add the first path value of "/home/ivan006/.virtualenvs/myproj/lib/python3.8/site-packages/django/contrib/admin/static/admin"
	- Reload your webapp
- Orient to 
	- Python anywheres web tab 
	- Static files section
- Action 
	- Add the second url value of "/static/"
	- Add the second path value of "/home/ivan006/b-python-course/first_project/static"
	- Reload your webapp
- Orient to 
	- Your pythonanywhere site 
- Action 
	- Add "/gobbledigook" to the end and it should say "The requested resource was not found on this server."

## Tools core function (views) (continued)

### Class based views 

- Orient to 
	- first_project
	- first_app
	- views.py
	- A new line after the "from django.contrib.auth.decorators import login_required" line 
- Action 
	- Add "from django.views.generic import View" 
- Orient to 
	- New line after ""
- Action 
	- Add 
		```
		class classview(View):
			def get(self, request):
				return HttpResponse("Hello world.")
		```
- Action 
	- Add a url called "classview" to the urls pointing to a view called like "views.classview.as_view()"
- Action 
	- 
- Orient to
  - Terminal (your working dir and env)
- Action
  - Run "python --version"
