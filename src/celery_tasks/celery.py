
from celery import Celery


celery_app = Celery(
    "celery_tasks",
    include = ['celery_tasks.tasks'],
    backend = "redis://localhost:6379/0",
    broker = "amqp://guest:@localhost:5672//"
)

celery_app.conf.beat_schedule = {
    'celery_beat_testing': {
        'task': 'clean_blog_like_count',
        'schedule': 24.0
    }
}

celery_app.conf.timezone = 'UTC'
celery_app.conf.update(task_track_started=True)
