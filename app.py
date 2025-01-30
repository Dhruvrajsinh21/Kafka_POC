import streamlit as st
from confluent_kafka import Consumer, KafkaException
import json

st.set_page_config(page_title="Kafka Log Viewer", layout="wide")
st.title("📜 Real-time Kafka Log Viewer")

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'log-consumer-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(conf)
consumer.subscribe(["logs"])

log_levels = ["ALL", "INFO", "WARNING", "ERROR", "DEBUG"]
selected_level = st.selectbox("Select log level", log_levels)

log_list = []
log_area = st.empty()

def filter_logs(log, selected_level):
    if selected_level == "ALL":
        return True
    return log['level'] == selected_level

def export_logs(log_list):
    with open("logs.txt", "w") as file:
        for log in log_list:
            file.write(log + "\n")
    st.success("Logs exported to logs.txt")

export_button = st.button("Export Logs to File")
if export_button:
    export_logs(log_list)

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        log = json.loads(msg.value().decode('utf-8'))
        if filter_logs(log, selected_level):
            log_entry = f"[{log['timestamp']}] **{log['level']}** - {log['message']} (Source: {log['source']})"
            log_list.insert(0, log_entry)
            log_area.text("\n".join(log_list[:20]))
            
except KeyboardInterrupt:
    st.write("Stopped.")
finally:
    consumer.close()
