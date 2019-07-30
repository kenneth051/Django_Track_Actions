# Track actions in a Django Applciation

[![Build Status](https://travis-ci.org/kenneth051/Django_Track_Actions.svg?branch=develop)](https://travis-ci.org/kenneth051/Django_Track_Actions)

[![Coverage Status](https://coveralls.io/repos/github/kenneth051/Django_Track_Actions/badge.svg?branch=develop)](https://coveralls.io/github/kenneth051/Django_Track_Actions?branch=develop)

This repo shows how to track applications in a django app using a middleware and signals.
We use the post save and post delete signal because I wanted to track the full object instance with the ID(Primary key) inclusive.

To try it out:

1- clone the repo

2- install the requirements

3- start the server (*python manage.py runserver*)

4- sign up

5- create a to-do item

6- edit the item and delete it 

7- visit the history endpoint

**endpoints**

                  sign up         |              http://127.0.0.1:8000/api/v1/users/

                  login           |              http://127.0.0.1:8000/api/v1/users/login/

             create and get Todo  |              http://127.0.0.1:8000/api/v1/todo

                history           |              http://127.0.0.1:8000/api/v1/history
