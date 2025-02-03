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

# (Producer 1)
def mysql_logs_producer():
    log_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "level": random.choice(log_levels),
        "message": "MySQL query log",
        "source": "MySQLProducer"
    }
    log_json = json.dumps(log_data)
    producer.produce("logs", key="mysql-log", value=log_json, callback=delivery_report)
    producer.flush()
    print(f"Sent MySQL Log: {log_data}")

# (Producer 2)
def nginx_logs_producer():
    log_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "level": random.choice(log_levels),
        "message": "NGINX error log",
        "source": "NGINXProducer"
    }
    log_json = json.dumps(log_data)
    producer.produce("nginxlogs", key="nginx-log", value=log_json, callback=delivery_report)
    producer.flush()
    print(f"Sent NGINX Log: {log_data}")

def start_random_producer():
    while True:
        selected_producer = random.choice([mysql_logs_producer, nginx_logs_producer])
        selected_producer()
        time.sleep(2) 

if __name__ == "__main__":
    try:
        start_random_producer()
    except KeyboardInterrupt:
        print("Producer stopped.")
