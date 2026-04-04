# Source: https://zipkin.io/pages/extensions_choices

Title: Server extensions and choices · OpenZipkin

URL Source: https://zipkin.io/pages/extensions_choices

Markdown Content:
Server extensions
-----------------

Zipkin server bundles extension for span collection and storage. By default spans can be collected over http, Kafka or RabbitMQ transports and stored in-memory or in MySQL, Cassandra or Elasticsearch.

The following modules add storage or transport extensions to the default server build. Please refer to their individual documentation for setup and configuration guides.

### OpenZipkin supported

The following extensions are supported by the OpenZipkin team and are hosted at the [OpenZipkin GitHub](https://github.com/openzipkin/) group. You can reach out to the team on [Zipkin Gitter](https://gitter.im/openzipkin/zipkin/) chat.

| Type | Module | Related product | Other notes |
| --- | --- | --- | --- |
| Collector | [zipkin-aws collector-sqs](https://github.com/openzipkin/zipkin-aws/tree/master/module#sqs-collector) | [AWS SQS](https://aws.amazon.com/sqs/) |  |
| Collector | [zipkin-aws collector-kinesis](https://github.com/openzipkin/zipkin-aws/tree/master/module#kinesis-collector) | [AWS Kinesis](https://aws.amazon.com/kinesis/) |  |
| Storage | [zipkin-aws storage-elasticsearch-aws](https://github.com/openzipkin/zipkin-aws/tree/master/module#elasticsearch-storage) | [AWS Elasticsearch Service](https://aws.amazon.com/elasticsearch-service/) |  |
| Storage | [zipkin-aws storage-xray](https://github.com/openzipkin/zipkin-aws/tree/master/module#xray-storage) | [AWS X-Ray](https://aws.amazon.com/xray/) | only supports sending to an XRay UDP daemon |
| Storage | [zipkin-gcp storage-stackdriver](https://github.com/openzipkin/zipkin-gcp/tree/master/storage-stackdriver) | [GCP Stackdriver](https://cloud.google.com/stackdriver/) | only supports sending to an Stackdriver |

| Type | Module | Related product | Other notes |
| --- | --- | --- | --- |
| Storage | [zipkin-storage-forwarder](https://github.com/openzipkin-contrib/zipkin-storage-forwarder) | [Apache kafka](https://kafka.apache.org/) (Optional) | Forwards spans to another HTTP or Kafka collector. |
| Storage | [zipkin-storage-kafka](https://github.com/openzipkin-contrib/zipkin-storage-kafka) | [Apache kafka](https://kafka.apache.org/) | Supports aggregation and indexing of tracing data via Kafka Streams State Store. |
| Reporter | [spring-cloud-sleuth-haystack-reporter](https://github.com/ExpediaDotCom/spring-cloud-sleuth-haystack-reporter) | [Haystack](https://github.com/ExpediaDotCom/haystack) | Supports sending data to Haystack, a resilient, scalable tracing and analysis system. |

Alternative servers
-------------------

The OpenZipkin team publish apis, data formats, and shared libraries that allow alternate backends to process the same data sent to the default Zipkin server.

Listed below are alternative backends that accept Zipkin format. Some use the same code as Zipkin on the same endpoints while others are on alternative endpoints or partially support features. In any case, the following aim to allow existing zipkin clients to use backends the OpenZipkin team does not support. Hence, direct questions to their respective communities.

*   [Apache SkyWalking](https://skywalking.apache.org/)
    *   When [zipkin trace component](https://skywalking.apache.org/docs/main/next/en/setup/backend/zipkin-trace/) is enabled, Skywalking exposes the same HTTP POST endpoints and Kafka topic Zipkin does 
        *   http port 9411 accepts `/api/v1/spans` (thrift, json) and `/api/v2/spans` (json, proto) POST requests.
        *   Kafka `zipkin` topic, and `zipkin` group ID accepts v2 spans encoded as a thrift/json/proto list per message.
        *   this extension uses the same encoding library and same endpoints as Zipkin does.

    *   Zipkin Lens UI is also bundled in SkyWalking booster UI since 9.4.0. `/zipkin` is exposed by SkyWalking webapp.

*   [Jaeger](https://github.com/jaegertracing/jaeger)
    *   When `COLLECTOR_ZIPKIN_HTTP_PORT=9411` is set, Jaeger exposes a partial implementation of Zipkin’s HTTP POST endpoints 
        *   http port 9411 accepts `/api/v1/spans` (thrift, json) and `/api/v2/spans` (json, proto) POST requests.

    *   When `SPAN_STORAGE_TYPE=kafka` and `zipkin-thrift`, Jaeger reads Zipkin v1 thrift encoded span messages from a Kafka topic. 
        *   Note: The above is a [deprecated practice](https://github.com/openzipkin/zipkin/tree/master/zipkin-collector/kafka#legacy-encoding) in Zipkin. Most instrumentation bundle multiple spans per message in v2 format.

*   [Pitchfork](https://github.com/HotelsDotCom/pitchfork)
    *   Pitchfork exposes the same HTTP POST endpoints Zipkin does 
        *   http port 9411 accepts `/api/v1/spans` (thrift, json) and `/api/v2/spans` (json, proto) POST requests.

Did we miss a server extension or alternative? Please open a pull-request to [openzipkin.github.io](https://github.com/openzipkin/openzipkin.github.io).
