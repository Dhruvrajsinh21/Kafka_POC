from confluent_kafka import Consumer, KafkaException
import json

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'log-consumer-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(conf)
consumer.subscribe(["logs"])

print("Listening for logs...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        log = json.loads(msg.value().decode('utf-8'))
        print(f"[{log['timestamp']}] {log['level']} - {log['message']} (Source: {log['source']})")

except KeyboardInterrupt:
    print("\nStopping consumer...")
finally:
    consumer.close()
