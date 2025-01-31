# Kafka POC

This is a Proof of Concept (POC) for integrating Apache Kafka with Streamlit to demonstrate real-time data streaming and here I created a producer which produces logs and through streamlit consumer app we can monitor the logs live.

## 1.Downloading and Setting Up Kafka

- Visit the Apache Kafka website and download the latest Kafka binary.
- Extract the downloaded Kafka package to your preferred directory.
- Apache Kafka website: https://kafka.apache.org/downloads

## 2. Start Zookeeper and Kafka

Go inside kafka file(C:\kafka_2.12-3.6.1) and open cmd and paste the following commands:
```console
cd bin
cd windows
zookeeper-server-start.bat ..\..\config\zookeeper.properties  ## Start Zookeeper
```
```console
#open new cmd for starting kafka-server
cd bin
cd windows
kafka-server-start.bat ..\..\config\server.properties
```
## 3. Clone the repository

```console
[git clone](https://github.com/Dhruvrajsinh21/Kafka_POC.git)
```
