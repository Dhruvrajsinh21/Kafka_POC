from confluent_kafka import Consumer, KafkaError
import json

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'image_consumer_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['image_topic'])

print("Listening for image data...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(f"Error: {msg.error()}")
            break

    image_data = json.loads(msg.value().decode('utf-8'))
    print(f"Received Image Data: {image_data}")
