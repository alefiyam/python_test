
A Simple Django Application
=================================
This application is simple Django application for demonstration of RESTful API .

Configuration details for this application
------------------------------------------

To configure this appliction into your local machine you must have installed python, MySql and pip package of python.

Once you have installed above requirements then follow these instruction to configure this application.

clone/download this application repository into your local machine.
then navigate to python_test directory and execute the following commands


```
$ pip install -r requirements.txt
```

this will install all required application depandancies.

To install the fake dummy data into the MySql database, firstly you need to create a database named as

	python_test

once you created database then run the following command to load the dummy data in your terminal

```
$ python manage.py loaddata api/fixtures/initial_data.json
```

this command will load the fake data into your all tables.

To start this application just run the following command

    python manage.py runserver

this will start the Django server, you can access the applicaiton on your browser using this url.

	http://localhost:8000/

create a superadmin by using command : python manage.py createsuperuser

Go on admin panel by url : http://localhost:8000/admin
and login by admin credentials 

In django oauth toolkit
create a application , select admin in user field,
confidential in client type
Resource owner password-based in authorization grant type

By following above steps application is created.
 
To create token use curl command :

curl -X POST -d "grant_type=password&username='<admin_username>'&password='<admin_password>'" -u '<client_id>:<client_secret>' 'localhost:8000/o/token/'

Mention clientid ,clientsecret ,admin username and password in above curl command
this will generate a token.

Set above generated token in settings.py file and start the application by 
python manage.py runserver.

