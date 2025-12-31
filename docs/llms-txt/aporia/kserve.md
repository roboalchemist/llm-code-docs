# Source: https://docs.aporia.com/storing-your-predictions/kserve.md

# Source: https://docs.aporia.com/v1/storing-your-predictions/kserve.md

# Source: https://docs.aporia.com/storing-your-predictions/kserve.md

# Source: https://docs.aporia.com/v1/storing-your-predictions/kserve.md

# Kubeflow / KServe

If you are using [Kubeflow](https://www.kubeflow.org/) or [KServe](https://github.com/kserve/kserve) for model serving, you can store the predictions of your models using InferenceDB.

[InferenceDB](https://github.com/aporia-ai/inferencedb) is an open-source cloud native tool that connects to KServe and streams predictions to a data lake, based on Kafka.

{% hint style="warning" %}
**WARNING: InferenceDB is still experimental!**

InferenceDB is an open-source project developed by Aporia. It is still experimental, and not yet ready for production!&#x20;
{% endhint %}

This guide will explain how to deploy a simple scikit-learn model using KServe, and log its inferences to a Parquet file in S3.

### Requirements

* [**KServe**](https://kserve.github.io/website/0.8/)
* [**KNative Eventing**](https://knative.dev/docs/eventing/) - with the [Kafka broker](https://knative.dev/docs/eventing/broker/kafka-broker/)
* [**Kafka**](https://kafka.apache.org/) - with Schema Registry, Kafka Connect, and [Confluent S3 Sink connector](https://docs.confluent.io/kafka-connect-s3-sink/current/overview.html) plugin

To get started as quickly as possible, see the [environment preperation tutorial](https://github.com/aporia-ai/inferencedb/wiki/KServe-Requirements), which shows how to set up a full environment in minutes.

### Step 1: Kafka Broker

First, we will need a Kafka broker to collect all KServe inference requests and responses:

```yaml
apiVersion: eventing.knative.dev/v1
kind: Broker
metadata:
  name: sklearn-iris-broker
  namespace: default
  annotations:
    eventing.knative.dev/broker.class: Kafka
spec:
  config:
    apiVersion: v1
    kind: ConfigMap
    name: inferencedb-kafka-broker-config
    namespace: knative-eventing
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: inferencedb-kafka-broker-config
  namespace: knative-eventing
data:
  # Number of topic partitions
  default.topic.partitions: "8"
  # Replication factor of topic messages.
  default.topic.replication.factor: "1"
  # A comma separated list of bootstrap servers. (It can be in or out the k8s cluster)
  bootstrap.servers: "kafka-cp-kafka.default.svc.cluster.local:9092"
```

### Step 2: InferenceService

Next, we will serve a simple sklearn model using KServe:

```yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: sklearn-iris
spec:
  predictor:
    logger:
      mode: all
      url: http://kafka-broker-ingress.knative-eventing.svc.cluster.local/default/sklearn-iris-broker
    sklearn:
      protocolVersion: v2
      storageUri: gs://seldon-models/sklearn/iris
```

Note the `logger` section - you can read more about it in the [KServe documentation](https://kserve.github.io/website/0.8/modelserving/logger/logger/).

### Step 3: InferenceLogger

Finally, we can log the predictions of our new model using InferenceDB:

```yaml
apiVersion: inferencedb.aporia.com/v1alpha1
kind: InferenceLogger
metadata:
  name: sklearn-iris
  namespace: default
spec:
  # NOTE: The format is knative-broker-<namespace>-<brokerName>
  topic: knative-broker-default-sklearn-iris-broker
  events:
    type: kserve
    config: {}
  destination:
    type: confluent-s3
    config:
      url: s3://aporia-data/inferencedb
      format: parquet

  # Optional - Only if you want to override column names
  schema:
    type: avro
    config:
      columnNames:
        inputs: [sepal_width, petal_width, sepal_length, petal_length]
        outputs: [flower]
```

### Step 4: Send requests

First, we will need to port-forward the Istio service so we can access it from our local machine:

```
kubectl port-forward --namespace istio-system svc/istio-ingressgateway 8080:80
```

Prepare a payload in a file called `iris-input.json`:

```json
{
  "inputs": [
    {
      "name": "input-0",
      "shape": [2, 4],
      "datatype": "FP32",
      "data": [
        [6.8, 2.8, 4.8, 1.4],
        [6.0, 3.4, 4.5, 1.6]
      ]
    }
  ]
}
```

And finally, you can send some inference requests:

```
SERVICE_HOSTNAME=$(kubectl get inferenceservice sklearn-iris -o jsonpath='{.status.url}' | cut -d "/" -f 3)

curl -v \
  -H "Host: ${SERVICE_HOSTNAME}" \
  -H "Content-Type: application/json" \
  -d @./iris-input.json \
  http://localhost:8080/v2/models/sklearn-iris/infer
```

### Step 5: Success!

If everything was configured correctly, these predictions should have been logged to a Parquet file in S3.

```python
import pandas as pd

df = pd.read_parquet("s3://aporia-data/inferencedb/default-sklearn-iris/")
print(df) 
```

[See the full example here.](https://github.com/aporia-ai/inferencedb/tree/main/examples/kserve/kafka-broker)
