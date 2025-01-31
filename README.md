# Kafka POC

This is a Proof of Concept (POC) for integrating Apache Kafka with Streamlit to demonstrate real-time data streaming and here I created a producer which produces logs and through streamlit consumer app we can monitor the logs live.

## 1. Downloading and Setting Up Kafka

- Visit the Apache Kafka website and download the latest Kafka binary.
- Extract the downloaded Kafka package to your preferred directory.
- Apache Kafka website: https://kafka.apache.org/downloads

## 2. Start Zookeeper and Kafka

Go inside kafka file(C:\kafka_2.12-3.6.1) and open cmd and paste the following commands:
```console
cd bin
cd windows
zookeeper-server-start.bat ..\..\config\zookeeper.properties  ## Started Zookeeper
```
Open new cmd of same path for starting kafka-server
```console
cd bin
cd windows
kafka-server-start.bat ..\..\config\server.properties ## Started Kafka-server
```
Open new cmd of same path for creating Kafka-topic
```console
cd bin
cd windows
kafka-topics.bat --create --topic logs --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 ## Created topic named logs
```
Don't stop until you want to stop the service

## 3. Clone the repository

```console
git clone https://github.com/Dhruvrajsinh21/Kafka_POC.git
```

## 4. Create Virtual environment and install requirements.txt

```console
python -m venv venv
source venv/bin/activate #On Windows use 'venv\Scripts\activate'
pip install -r requirements.txt
```

## 5. Run the producer

```console
python producer.py
```

## 6. Run the streamlit consumer app.py

```console
streamlit run app.py
```

