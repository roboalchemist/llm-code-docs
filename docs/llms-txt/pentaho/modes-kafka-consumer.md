# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/options-kafka-consumer/offset-settings-tab/modes-kafka-consumer.md

# Modes

You can run the Kafka consumer step in three different modes using the Offset Settings tab.

* Infinite loop
* End Timestamp to stop consumer
* Read data between two-time stamps

## Infinite loop

If you do not enter a value in the **Offset timestamp** field, the Kafka consumer runs in an infinite loop by default.

## End Timestamp to stop consumer

When you enter a value in **Offset timestamp** field, it is considered as the end time and the consumer stops when it reaches that time.

## Read data between two timestamps

By using the Kafka consumer step in conjunction with the Kafka Offset job, you can consume data between a start time and an end time, using either secure or non-secure connections. The **Offset timestamp** value in the Kafka Offset job is considered the start time and the **Offset timestamp** value in the Kafka Consumer step is considered the end time.

For example, if you set the **Offset timestamp** value in the Kafka Offset job to `23/08/02 07:03:00` and set the **Offset timestamp** value in the Kafka consumer step to `23/08/04 07:03:00`, you will consume the data for a 48 hour period.

**Note:** The Kafka Offset job resets the offset of all the partitions in the topic of consumer group according to the job **Offset timestamp**.

This`kafka_job.kjb` sample shown below is located in the `design-tools/data-integration/plugins/pentaho-streaming-kafka-plugin-zip-9.5.1.0-110/pentaho-streaming-kafka-plugin/samples/transformations` directory and demonstrates using the Kafka Offset job with the Kafka consumer step

![Kafka Offset Job with consumer example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6f130ae3399c93be3d030e5bf469ce7a51596fb8%2FPDI%20Kafka_Job%20example%20.png?alt=media)
