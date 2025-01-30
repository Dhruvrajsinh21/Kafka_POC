from confluent_kafka import Producer
import json
import time
import random

conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def send_logs():
    while True:
        log_data = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "level": random.choice(log_levels),
            "message": "Sample log message",
            "source": "KafkaProducer"
        }
        log_json = json.dumps(log_data)
        producer.produce("logs", key="log", value=log_json, callback=delivery_report)
        producer.flush()
        print(f"Sent log: {log_data}")
        time.sleep(2)

send_logs()
