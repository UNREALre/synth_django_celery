# -*- coding: utf-8 -*-

import requests
import concurrent.futures

from datetime import timedelta
from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

app.conf.beat_schedule = {
    'add-every-2-minutes1': {
        'task': 'tasks2.demo1',
        'schedule': timedelta(minutes=2),
    },
    'add-every-2-minutes2': {
        'task': 'tasks2.demo2',
        'schedule': timedelta(minutes=2),
    },
    'add-every-2-minutes3': {
        'task': 'tasks2.demo3',
        'schedule': timedelta(minutes=2),
    },
    'add-every-2-minutes4': {
        'task': 'tasks2.demo4',
        'schedule': timedelta(minutes=2),
    },
    'add-every-2-minutes5': {
        'task': 'tasks2.demo5',
        'schedule': timedelta(minutes=2),
    },
}


@app.task(time_limit=120)
def demo1():
    make_request(1)


@app.task(time_limit=120)
def demo2():
    make_request(2)


@app.task(time_limit=120)
def demo3():
    make_request(3)


@app.task(time_limit=120)
def demo4():
    make_request(4)


@app.task(time_limit=120)
def demo5():
    make_request(5)


def make_request(param):
    requests.get(f'http://127.0.0.1:8000/api/test/?id={param}')
