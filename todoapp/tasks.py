from celery import shared_task
from time import sleep
from PIL import Image


@shared_task(name="first-task")
def add(x, y):
    sleep(20)
    print(x+y)


@shared_task(name="thumbnail_creator")
def thumbnail_creator_task(image):
    sleep(10)
    pil_image = Image.open(image)
    pil_image.resize((100, 100))
    pil_image.save("temp.jpg")
