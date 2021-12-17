from celery import shared_task
from time import sleep


@shared_task(name="first-task")
def add(x, y):
    sleep(20)
    print(x+y)
