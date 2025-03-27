import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'r_project.settings')
app = Celery('r_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.worker_pool = "solo"
app.conf.broker_connection_retry_on_startup = True
app.autodiscover_tasks()
