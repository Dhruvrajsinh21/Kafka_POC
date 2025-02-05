from confluent_kafka import Consumer
import json
import os
from PIL import Image

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "logs"
GROUP_ID = "thumbnail_group"

consumer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': GROUP_ID,
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False 
}

consumer = Consumer(consumer_conf)
consumer.subscribe([TOPIC_NAME])

THUMBNAIL_SIZE = (200, 200)
SAVE_PATH = "thumbnails/"

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

def generate_thumbnail(image_path, image_name):
    try:
        new_name = os.path.join(SAVE_PATH, f"{image_name.split('.')[0]}_thumbnail.jpg")
        if os.path.exists(new_name):
            print(f"Thumbnail already exists: {new_name}")
            return

        with Image.open(image_path) as img:
            img.thumbnail(THUMBNAIL_SIZE)
            img.save(new_name)
            print(f"Thumbnail saved as {new_name}")

    except Exception as e:
        print(f"Error processing {image_name}: {e}")

print("Listening for image processing requests...")

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        try:
            data = json.loads(msg.value().decode('utf-8'))
            generate_thumbnail(data["image_path"], data["image_name"])
            consumer.commit()
        
        except json.JSONDecodeError:
            print("Error: Received invalid JSON message.")

except KeyboardInterrupt:
    print("Shutting down consumer...")

finally:
    consumer.close()
    print("Consumer closed.")
