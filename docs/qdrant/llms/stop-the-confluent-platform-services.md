# Stop the Confluent Platform services:
confluent local stop

```

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#installation-of-qdrant) Installation of Qdrant:

To install and run Qdrant (self-managed locally), you can use Docker, which simplifies the process. First, ensure you have Docker installed on your system. Then, you can pull the Qdrant image from Docker Hub and run it with the following commands:

```bash
docker pull qdrant/qdrant
docker run -p 6334:6334 -p 6333:6333 qdrant/qdrant

```

This will download the Qdrant image and start a Qdrant instance accessible at `http://localhost:6333`. For more detailed instructions and alternative installation methods, refer to the [Qdrant installation documentation](https://qdrant.tech/documentation/quick-start/).

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#installation-of-qdrant-kafka-sink-connector) Installation of Qdrant-Kafka Sink Connector:

To install the Qdrant Kafka connector using [Confluent Hub](https://www.confluent.io/hub/), you can utilize the straightforward `confluent-hub install` command. This command simplifies the process by eliminating the need for manual configuration file manipulations. To install the Qdrant Kafka connector version 1.1.0, execute the following command in your terminal:

```bash
 confluent-hub install qdrant/qdrant-kafka:1.1.0

```

This command downloads and installs the specified connector directly from Confluent Hub into your Confluent Platform or Kafka Connect environment. The installation process ensures that all necessary dependencies are handled automatically, allowing for a seamless integration of the Qdrant Kafka connector with your existing setup. Once installed, the connector can be configured and managed using the Confluent Control Center or the Kafka Connect REST API, enabling efficient data streaming between Kafka and Qdrant without the need for intricate manual setup.

![2.webp](https://qdrant.tech/documentation/examples/data-streaming-kafka-qdrant/2.webp)

_Figure 2: Local Confluent platform showing the Source and Sink connectors after installation._

Ensure the configuration of the connector once it’s installed as below. keep in mind that your `key.converter` and `value.converter` are very important for kafka to safely deliver the messages from topic to qdrant.

```bash
{
  "name": "QdrantSinkConnectorConnector_0",
  "config": {
    "value.converter.schemas.enable": "false",
    "name": "QdrantSinkConnectorConnector_0",
    "connector.class": "io.qdrant.kafka.QdrantSinkConnector",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "topics": "topic_62,qdrant_kafka.docs",
    "errors.deadletterqueue.topic.name": "dead_queue",
    "errors.deadletterqueue.topic.replication.factor": "1",
    "qdrant.grpc.url": "http://localhost:6334",
    "qdrant.api.key": "************"
  }
}

```

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#installation-of-mongodb) Installation of MongoDB

For the Kafka to connect MongoDB as source, your MongoDB instance should be running in a `replicaSet` mode. below is the `docker compose` file which will spin a single node `replicaSet` instance of MongoDB.

```bash
version: "3.8"

services:
  mongo1:
    image: mongo:7.0
    command: ["--replSet", "rs0", "--bind_ip_all", "--port", "27017"]
    ports:
      - 27017:27017
    healthcheck:
      test: echo "try { rs.status() } catch (err) { rs.initiate({_id:'rs0',members:[{_id:0,host:'host.docker.internal:27017'}]}) }" | mongosh --port 27017 --quiet
      interval: 5s
      timeout: 30s
      start_period: 0s
      start_interval: 1s
      retries: 30
    volumes:
      - "mongo1_data:/data/db"
      - "mongo1_config:/data/configdb"

volumes:
  mongo1_data:
  mongo1_config:

```

Similarly, install and configure source connector as below.

```bash
confluent-hub install mongodb/kafka-connect-mongodb:latest

```

After installing the `MongoDB` connector, connector configuration should look like this:

```bash
{
  "name": "MongoSourceConnectorConnector_0",
  "config": {
    "connector.class": "com.mongodb.kafka.connect.MongoSourceConnector",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "value.converter": "org.apache.kafka.connect.storage.StringConverter",
    "connection.uri": "mongodb://127.0.0.1:27017/?replicaSet=rs0&directConnection=true",
    "database": "qdrant_kafka",
    "collection": "docs",
    "publish.full.document.only": "true",
    "topic.namespace.map": "{\"*\":\"qdrant_kafka.docs\"}",
    "copy.existing": "true"
  }
}

```

## [Anchor](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/\#playground-application) Playground Application

As the infrastructure set is completely done, now it’s time for us to create a simple application and check our setup. the objective of our application is the data is inserted to Mongodb and eventually it will get ingested into Qdrant also using [Change Data Capture (CDC)](https://www.confluent.io/learn/change-data-capture/).

`requirements.txt`

```bash
fastembed==0.3.1
pymongo==4.8.0
qdrant_client==1.10.1

```

`project_root_folder/main.py`

This is just sample code. Nevertheless it can be extended to millions of operations based on your use case.

pythonpython

```python
from pymongo import MongoClient
from utils.app_utils import create_qdrant_collection
from fastembed import TextEmbedding

collection_name: str = 'test'
embed_model_name: str = 'snowflake/snowflake-arctic-embed-s'

```

```python