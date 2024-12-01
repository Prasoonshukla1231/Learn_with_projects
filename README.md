# Tood_ app in django


#. Setup
To get this repository, run the following command inside your git enabled terminal
https://github.com/Prasoonshukla1231/Learn_with_projects/edit/main/README.md#tood_-app-in-django

You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide.
After download django you will install virtual enviroment pip install virtualenv
Create Django Project - $ django-admin startproject Todo_site

migration in django -  $ python manage.py makemigrations
This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command

$ python manage.py migrate
One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user

$ python manage.py createsuperuser


#. Run Project.

Run project using this command- $ python manage.py runserver

 Once the server hosted, Todo app  Project run successfully.

 Well Done...👍👍👍




