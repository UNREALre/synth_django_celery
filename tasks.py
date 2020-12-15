# -*- coding: utf-8 -*-

import requests
import concurrent.futures

from datetime import timedelta
from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

app.conf.beat_schedule = {
    'add-every-2-minutes': {
        'task': 'tasks.demo',
        'schedule': timedelta(minutes=2),
    },
}


@app.task(time_limit=60)
def demo():
    queue = [i for i in range(7500)]
    for item in queue:
        make_request(item)

    #with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
    #    executor.map(make_request, queue)


def make_request(param):
    requests.get(f'http://127.0.0.1:8000/api/test/?id={param}')
