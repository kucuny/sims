#!/bin/bash

poetry install
python app/manage.py migrate
python app/manage.py runserver 0.0.0.0:8000
