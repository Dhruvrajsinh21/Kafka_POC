from confluent_kafka import Producer
import json
import os
import time
import random
from PIL import Image

conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

IMAGE_DIR = "images/"
THUMBNAIL_DIR = "thumbnails/"

os.makedirs(THUMBNAIL_DIR, exist_ok=True)

def create_thumbnail(image_path):
    img = Image.open(image_path)
    img.thumbnail((100, 100))
    base_name = os.path.basename(image_path)
    thumb_name = f"thumb_{base_name}"
    thumb_path = os.path.join(THUMBNAIL_DIR, thumb_name)
    img.save(thumb_path)
    return thumb_path

def send_image_data():
    for image_file in os.listdir(IMAGE_DIR):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            original_path = os.path.join(IMAGE_DIR, image_file)
            thumb_path = create_thumbnail(original_path)

            # Kafka Message
            image_data = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "original_image": original_path,
                "thumbnail_image": thumb_path
            }
            producer.produce("image_topic", key="image-log", value=json.dumps(image_data))
            producer.flush()
            print(f"Sent Image Data: {image_data}")

if __name__ == "__main__":
    send_image_data()
