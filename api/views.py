# -*- coding: utf-8 -*-

import os
import threading

from rest_framework import views
from rest_framework.response import Response
from time import sleep
from random import randint, seed, random


def load_heavy_data():
    seconds = randint(2, 4)
    f = open('api.log', 'a')
    f.write(f'loading data for {seconds} seconds ...\n')
    f.close()
    sleep(seconds)


class SynthTest(views.APIView):

    def get(self, request):
        sleep(random())

        pid = os.getpid()
        f = open('api.log', 'a')
        f.write(f'pid #{pid}, thread #{threading.get_ident()} - {request.GET.get("id")} - beat ...\n')
        f.close()

        # load_heavy_data()

        data = {"answer": f"processed request #{request.GET.get('id')}"}
        return Response(data)
