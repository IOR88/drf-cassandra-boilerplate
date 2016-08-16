#!/usr/bin/env bash
./conf/wait-for-it.sh -t 20 cassandra:9042
python manage.py runserver 0.0.0.0:8000