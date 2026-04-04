# [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#setup-data-streaming-with-kafka-via-confluent) Setup Data Streaming with Kafka via Confluent

**Author:** [M K Pavan Kumar](https://www.linkedin.com/in/kameshwara-pavan-kumar-mantha-91678b21/) , research scholar at [IIITDM, Kurnool](https://iiitk.ac.in/). Specialist in hallucination mitigation techniques and RAG methodologies.
• [GitHub](https://github.com/pavanjava) • [Medium](https://medium.com/@manthapavankumar11)

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#introduction) Introduction

This guide will walk you through the detailed steps of installing and setting up the [Qdrant Sink Connector](https://github.com/qdrant/qdrant-kafka), building the necessary infrastructure, and creating a practical playground application. By the end of this article, you will have a deep understanding of how to leverage this powerful integration to streamline your data workflows, ultimately enhancing the performance and capabilities of your data-driven real-time semantic search and RAG applications.

In this example, original data will be sourced from Azure Blob Storage and MongoDB.

![1.webp](https://qdrant.tech/documentation/examples/data-streaming-kafka-qdrant/1.webp)

Figure 1: [Real time Change Data Capture (CDC)](https://www.confluent.io/learn/change-data-capture/) with Kafka and Qdrant.

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#the-architecture) The Architecture:

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#source-systems) Source Systems

The architecture begins with the **source systems**, represented by MongoDB and Azure Blob Storage. These systems are vital for storing and managing raw data. MongoDB, a popular NoSQL database, is known for its flexibility in handling various data formats and its capability to scale horizontally. It is widely used for applications that require high performance and scalability. Azure Blob Storage, on the other hand, is Microsoft’s object storage solution for the cloud. It is designed for storing massive amounts of unstructured data, such as text or binary data. The data from these sources is extracted using **source connectors**, which are responsible for capturing changes in real-time and streaming them into Kafka.

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#kafka) Kafka

At the heart of this architecture lies **Kafka**, a distributed event streaming platform capable of handling trillions of events a day. Kafka acts as a central hub where data from various sources can be ingested, processed, and distributed to various downstream systems. Its fault-tolerant and scalable design ensures that data can be reliably transmitted and processed in real-time. Kafka’s capability to handle high-throughput, low-latency data streams makes it an ideal choice for real-time data processing and analytics. The use of **Confluent** enhances Kafka’s functionalities, providing additional tools and services for managing Kafka clusters and stream processing.

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#qdrant) Qdrant

The processed data is then routed to **Qdrant**, a highly scalable vector search engine designed for similarity searches. Qdrant excels at managing and searching through high-dimensional vector data, which is essential for applications involving machine learning and AI, such as recommendation systems, image recognition, and natural language processing. The **Qdrant Sink Connector** for Kafka plays a pivotal role here, enabling seamless integration between Kafka and Qdrant. This connector allows for the real-time ingestion of vector data into Qdrant, ensuring that the data is always up-to-date and ready for high-performance similarity searches.

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#integration-and-pipeline-importance) Integration and Pipeline Importance

The integration of these components forms a powerful and efficient data streaming pipeline. The **Qdrant Sink Connector** ensures that the data flowing through Kafka is continuously ingested into Qdrant without any manual intervention. This real-time integration is crucial for applications that rely on the most current data for decision-making and analysis. By combining the strengths of MongoDB and Azure Blob Storage for data storage, Kafka for data streaming, and Qdrant for vector search, this pipeline provides a robust solution for managing and processing large volumes of data in real-time. The architecture’s scalability, fault-tolerance, and real-time processing capabilities are key to its effectiveness, making it a versatile solution for modern data-driven applications.

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#installation-of-confluent-kafka-platform) Installation of Confluent Kafka Platform

To install the Confluent Kafka Platform (self-managed locally), follow these 3 simple steps:

**Download and Extract the Distribution Files:**

- Visit [Confluent Installation Page](https://www.confluent.io/installation/).
- Download the distribution files (tar, zip, etc.).
- Extract the downloaded file using:

```bash
tar -xvf confluent-<version>.tar.gz

```

or

```bash
unzip confluent-<version>.zip

```

**Configure Environment Variables:**

```bash