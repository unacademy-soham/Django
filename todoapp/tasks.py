from celery import shared_task
from time import sleep
from PIL import Image
from base64 import b64decode


@shared_task(name="first-task")
def add(x, y):
    sleep(20)
    print(x+y)


@shared_task(name="thumbnail_creator")
def thumbnail_creator_task(file_id):
    sleep(10)
    pil_image = Image.open("todoapp/images/" + file_id + ".jpg")
    pil_image.resize((100, 100))
    pil_image.save("temp.jpg")
