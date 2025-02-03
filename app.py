import streamlit as st
from confluent_kafka import Consumer, KafkaError
import json
import threading
import queue

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'log_consumer_group',
    'auto.offset.reset': 'earliest'
}

log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]

log_queue = queue.Queue()

def consume_mysql_logs(selected_level):
    consumer = Consumer(conf)
    consumer.subscribe(['logs'])
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
        log_data = json.loads(msg.value().decode('utf-8'))
        log_level = log_data.get('level', 'INFO')
        if selected_level == 'All' or log_level == selected_level:
            log_queue.put(f"**MySQL Log - Level: {log_level}:** {log_data}")

def consume_nginx_logs(selected_level):
    consumer = Consumer(conf)
    consumer.subscribe(['nginxlogs'])
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
        log_data = json.loads(msg.value().decode('utf-8'))
        log_level = log_data.get('level', 'INFO')
        if selected_level == 'All' or log_level == selected_level:
            log_queue.put(f"**NGINX Log - Level: {log_level}:** {log_data}")

st.title("Kafka Consumer Stream")

log_type = st.selectbox("Select Log Type", ["MySQL Logs", "NGINX Logs"])

log_level = st.selectbox("Select Log Level", ["All", "INFO", "WARNING", "ERROR", "DEBUG"])

def start_consumer(log_type, log_level):
    if log_type == "MySQL Logs":
        thread = threading.Thread(target=consume_mysql_logs, args=(log_level,))
        thread.daemon = True 
        thread.start()
    elif log_type == "NGINX Logs":
        thread = threading.Thread(target=consume_nginx_logs, args=(log_level,))
        thread.daemon = True 
        thread.start()

def display_logs():
    while True:
        if not log_queue.empty():
            log_message = log_queue.get()
            st.write(log_message)

if st.button("Start Consumer"):
    start_consumer(log_type, log_level)
    st.success(f"{log_type} Consumer started!")
    display_logs()
