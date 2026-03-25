# Source: https://docs.pinot.apache.org/release-0.4.0/plugins/pinot-input-format.md

# Pinot Input Format

Pinot Input format is a set of plugins with the goal of reading data from files during data ingestion. It can be split into two additional types: record encoders (for batch jobs) and decoders (for ingestion).

Currently supported Pinot Input Formats:

* Batch
  * Avro
  * CSV
  * JSON
  * ORC
  * PARQUET
  * THRIFT
* Streaming
  * Avro
  * Avro Confluent
    * To use the avro confluent stream decoder, the realtime table configuration should point to the `streamConfigs` section of `tableIndexConfig` should point to the avro confluent stream decoder. Here is an example configuration:

```
"streamConfigs": {
  "streamType": "kafka",
  "stream.kafka.consumer.type": "LowLevel",
  "stream.kafka.topic.name": "kafka-topic",
  "stream.kafka.decoder.class.name": "org.apache.pinot.plugin.inputformat.avro.confluent.KafkaConfluentSchemaRegistryAvroMessageDecoder",
  "stream.kafka.consumer.factory.class.name": "org.apache.pinot.plugin.stream.kafka20.KafkaConsumerFactory",
  "stream.kafka.decoder.prop.schema.registry.rest.url": "http://<schema registry host>:8081",
  "stream.kafka.zk.broker.url": "<zk broker url>/",
  "stream.kafka.broker.list": "<kafka broker url>",
  "realtime.segment.flush.threshold.time": "24h",
  "realtime.segment.flush.threshold.size": "0",
  "realtime.segment.flush.desired.size": "150M",
  "stream.kafka.consumer.prop.auto.isolation.level": "read_committed",
  "stream.kafka.consumer.prop.auto.offset.reset": "smallest",
  "stream.kafka.consumer.prop.group.id": "<group id>",
  "stream.kafka.consumer.prop.client.id": "<client id>"
}
```

�

* Protocol Buffers\
  To ingest data in protocol buffers format, the following config needs to be added in the ingestion spec

  ```
  executionFrameworkSpec:
    name: 'standalone'
    segmentGenerationJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentGenerationJobRunner'
    segmentTarPushJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentTarPushJobRunner'
    segmentUriPushJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentUriPushJobRunner'
  jobType: SegmentCreationAndTarPush
  inputDirURI: 'file:///path/to/input'
  includeFileNamePattern: 'glob:**/*.parquet'
  excludeFileNamePattern: 'glob:**/*.avro'
  outputDirURI: 'file:///path/to/output'
  overwriteOutput: true
  pinotFSSpecs:
    - scheme: file
      className: org.apache.pinot.spi.filesystem.LocalPinotFS
  recordReaderSpec:
    dataFormat: 'proto'
    className: 'org.apache.pinot.plugin.inputformat.protobuf.ProtoBufRecordReader'
    configClassName: 'org.apache.pinot.plugin.inputformat.protobuf.ProtoBufRecordReaderConfig'
    configs:
      descriptorFile: 'file:///path/to/sample.desc
  tableSpec:
    tableName: 'myTable'
    schemaURI: 'http://localhost:9000/tables/myTable/schema'
    tableConfigURI: 'http://localhost:9000/tables/myTable'
  pinotClusterSpecs:
    - controllerURI: 'localhost:9000'
  pushJobSpec:
    pushAttempts: 2
  ```

The **descriptorFile** contains all of the descriptors of a .**proto** file. It should be an URI pointing to the location of the .**desc** file for a corresponding .**proto** file. You can generate the descriptor file from a .proto file using the command

`protoc -I=/directory/containing/proto/files--include_imports -- descriptor_set_out=/path/to/sample.desc /path/to/sample.proto`
