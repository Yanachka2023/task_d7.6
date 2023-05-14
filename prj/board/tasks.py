from celery import Celery
from celery import shared_task
from prj.newapp.models import Category
import time

app = Celery('task', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

@shared_task
def send_mail():
    for x in  Category.objects.all():
        for s in x.sub.all():
            send_mail(
                'Subject here',
                'Here is the message',
                'alsakeluei@yandex.com',
                [s.mail],
                fail_silently=False,
            )

@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")