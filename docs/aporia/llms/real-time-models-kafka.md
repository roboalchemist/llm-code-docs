# Source: https://docs.aporia.com/storing-your-predictions/real-time-models-kafka.md

# Source: https://docs.aporia.com/v1/storing-your-predictions/real-time-models-kafka.md

# Real-time Models (Kafka)

For high-throughput, real-time models (e.g models with an HTTP endpoint such as `POST /predict` and billions of predictions per day), you can stream predictions to [Kafka](https://kafka.apache.org/) or other message brokers, and then have a separate process to store them in a persistent storage.

Using a message broker such as Kafka lets you store predictions of real-time models with low latency.

{% hint style="info" %}
**Don't have billions of predictions?**

If you are not dealing with billions of predictions per day, you should consider a simpler solution.

Please see the guide on [real-time models with Postgres](https://docs.aporia.com/v1/storing-your-predictions/real-time-models-postgres).
{% endhint %}

### Step 1: Deploy Kafka

You can deploy Kafka in various ways:

* If you are using Kubernetes, you can deploy the [Confluent Helm charts](https://github.com/confluentinc/cp-helm-charts) or the [Strimzi operator](https://strimzi.io/).
* Deploy a managed Kafka service in your cloud provider, e.g [AWS MSK](https://aws.amazon.com/msk/).
* Use a managed service such as [Confluent](https://www.confluent.io/).

### Step 2: Write predictions to Kafka

Writing messages to a Kafka queue is very simple in Python and other languages. Here are examples for Flask and FastAPI, which are commonly used to serve ML models.

#### Flask

With Flask, you can use the [kafka-python](https://kafka-python.readthedocs.io/en/master/) library. Example:

```python
producer = KafkaProducer(bootstrap_servers="kafka-cp-kafka:9092")

@app.route("/predict", methods=["POST"])
def predict():
  ...

  producer.send("my-model", json.dumps({
    "id": str(uuid.uuid4()),
    "model_name": "my-model",
    "model_version": "v1",
    "inputs": {
      "age": 38,
      "previously_insured": True,
    },
    "outputs": {
      "will_buy_insurance": True,
      "confidence": 0.98,
    },
  }).encode("ascii"))    
```

#### FastAPI

With async FastAPI, you can use the [aiokafka](https://aiokafka.readthedocs.io/en/stable/) library. First, initialize a new Kafka producer:

```python
aioproducer = None

@app.on_event("startup")
async def startup_event():
  global aioproducer
  aioproducer = AIOKafkaProducer(bootstrap_servers="my-kafka:9092")

  await aioproducer.start()


@app.on_event("shutdown")
async def shutdown_event():
  await aioproducer.stop()
```

Then, whenever you have a new prediction you can publish it to a Kafka topic:

```python
@app.post("/predict")
async def predict(request: PredictRequest):
  ...

  await aioproducer.send("my-model", json.dumps({
    "id": str(uuid.uuid4()),
    "model_name": "my-model",
    "model_version": "v1",
    "inputs": {
      "age": 38,
      "previously_insured": True,
    },
    "outputs": {
      "will_buy_insurance": True,
      "confidence": 0.98,
    },
  }).encode("ascii"))
```

### Step 3: Stream to a Persistent Storage

Now, you can stream predictions from Kafka to a persistent storage such as S3. There are different ways to achieve this - we'll cover here [Kafka Connect](https://docs.confluent.io/platform/current/connect/index.html) and [Spark Streaming](https://spark.apache.org/docs/latest/streaming-programming-guide.html).

#### Spark Streaming

Spark Streaming is an extension of the core Spark API that allows you to process real-time data from various sources including Kafka. This processed data can be pushed out to file systems and databases.

In this example, we will process messages from the `my-model` topic and store them in a Delta lake table:

```python
# Create stream with Kafka source
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "my-kafka:9092") \
    .option("subscribe", "my-model") \
    .option("startingOffsets", "earliest") \
    .option("failOnDataLoss", "false") \
    .load()


# Parse JSON from Kafka
schema = StructType() \
    .add("sepal_length", FloatType()) \
    .add("sepal_width", FloatType()) \
    .add("petal_length", FloatType()) \
    .add("petal_width", FloatType()) \
    .add("prediction", IntegerType()) \
    .add("confidence", FloatType())

df = df.withColumn("json", F.from_json(F.col("value").cast("string"), schema))
df = df.select(F.col("json.*"))


# Write to Delta Lake
df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("mergeSchema", "true") \
    .option("checkpointLocation", f"{S3_BASE_URL}/my-model/serving/_checkpoints/kafka") \
    .start(f"{S3_BASE_URL}/my-model/serving") \
    .awaitTermination()
```

#### Kafka Connect

Kafka Connect makes it easy to quickly define connectors to move data between Kafka and other data systems, such as S3, Elasticsearch, and others.

As a prerequisite to Kafka Connect, you'll need [Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html), which is a tool to manage schemas for Kafka topics.

Here is an example of a connector to stream messages from the `my-model` topic to Parquet file on S3:

```json
PUT /connectors/my-model-connector/config

{
  "connector.class": "io.confluent.connect.s3.S3SinkConnector",
  "storage.class": "io.confluent.connect.s3.storage.S3Storage",
  "s3.region": "us-east-1",
  "s3.bucket.name": "myorg-models",
  "topics.dir": "my-model/serving",
  "flush.size": "2",
  "rotate.schedule.interval.ms": "20000",
  "auto.register.schemas": "false",
  "tasks.max": "1",
  "s3.part.size": "5242880",
  "timezone": "UTC",
  "parquet.codec": "snappy",
  "topics": "my-model",
  "s3.credentials.provider.class": "com.amazonaws.auth.DefaultAWSCredentialsProviderChain",
  "format.class": "parquet",
  "value.converter": "org.apache.kafka.connect.json.JsonConverter",
  "key.converter": "org.apache.kafka.connect.storage.StringConverter",
  "schema.registry.url": "http://my-schema-registry",
  "value.converter.schema.registry.url": "http://my-schema-registry"
}
```
