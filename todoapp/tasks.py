from celery import shared_task
from time import sleep

@shared_task(name="first-task")
def add(x, y):
    sleep(20)
    print(x+y)


@shared_task(name="image_uploader")
def item_image_upload(file_name, item_id):
    # Upload the image to s3. Make sure it is publicly available
    # Get the public url for the image
    # Update the ItemImage database with url and item_id
    pass


@shared_task(name="review_image_uploader")
def review_image_upload(file_name, review_id):
    # Upload the image to s3. Make sure it is publicly available
    # Get the public url for the image
    # Update the ItemImage database with url and item_id
    pass
