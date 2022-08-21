from celery import Celery
import os


app = Celery('tasks', backend=os.environ.get('REDIS_BROKER_URL'))

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
    result_expires=3600,
)
app.autodiscover_tasks()


