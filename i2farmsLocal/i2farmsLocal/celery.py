from argparse import Namespace
import os
from celery import Celery
from django.conf import settings

#default django settings module for 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'i2farmsLocal.settings')

app = Celery('i2farmsLocal', broker='pyamqp://guest@localhost//')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request : {self.request!r}')