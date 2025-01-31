# kafka POC

This is a Proof of Concept (POC) for integrating Apache kafka with Streamlit to demonstrate real-time data streaming. In this setup, I created a producer that generates logs, and through the Streamlit consumer app, we can monitor the logs live. 

## Follow the below mentioned steps for setting up and running the Kafka POC app locally:

### 1. Downloading and Setting Up kafka 

- Visit the Apache kafka website and download the latest Kafka binary.
- Extract the downloaded Kafka package to your preferred directory.
- Apache kafka website: https://kafka.apache.org/downloads

### 2. Start Zookeeper and kafka

Go inside kafka folder (C:\kafka_2.12-3.6.1) and open cmd and paste the following commands:
```console
cd bin
cd windows
zookeeper-server-start.bat ..\..\config\zookeeper.properties  # Started Zookeeper
```
Open new cmd in the same folder for starting kafka-server
```console
cd bin
cd windows
kafka-server-start.bat ..\..\config\server.properties # Started kafka-server
```
Open new cmd in the same folder for creating kafka-topic
```console
cd bin
cd windows
kafka-topics.bat --create --topic logs --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 # Created topic named logs
```
**Do not stop the above services unless you no longer want to use the app.**

### 3. Clone the repository

```console
git clone https://github.com/Dhruvrajsinh21/Kafka_POC.git
```

### 4. Create Virtual environment and install requirements.txt

```console
python -m venv venv
source venv/bin/activate # On Windows use 'venv\Scripts\activate'
pip install -r requirements.txt
```

### 5. Run the producer

```console
python producer.py
```

### 6. Run the streamlit consumer app.py

```console
streamlit run app.py
```

## Streamlit app
![image](https://github.com/user-attachments/assets/7dc0cdca-f18e-4f22-9063-83c5fad8e7da)
## Producer
![image](https://github.com/user-attachments/assets/4f1311a3-54dd-4b34-9ad8-7ecbb9443835)
## Consumer
![image](https://github.com/user-attachments/assets/50b0eebb-d552-4600-ada1-63a1771d5431)


