from celery import shared_task
from time import sleep
from PIL import Image
from base64 import b64decode


@shared_task(name="first-task")
def add(x, y):
    sleep(20)
    print(x+y)


@shared_task(name="thumbnail_creator")
def thumbnail_creator_task(base64_image):
    sleep(10)
    image = b64decode(base64_image)
    pil_image = Image.open(image)
    pil_image.resize((100, 100))
    pil_image.save("temp.jpg")
