from confluent_kafka import Producer
import json
import os

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "logs"

UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

conf = {'bootstrap.servers': KAFKA_BROKER}
producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def send_image_to_kafka(image_path):
    if not os.path.exists(image_path):
        print(f"Error: {image_path} does not exist.")
        return

    image_name = os.path.basename(image_path)
    message = json.dumps({
        "image_path": image_path,
        "image_name": image_name
    })

    producer.produce(TOPIC_NAME, value=message, callback=delivery_report)
    producer.flush()

    print(f"Sent image {image_name} to Kafka.")
