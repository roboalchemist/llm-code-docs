# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/options-kafka-consumer/offset-settings-tab.md

# Offset Settings tab

![Kafka consumer Offset Settings tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-5120326da6573e47b3b7de3783a5542668844ac8%2FPDI%20Kafka%20consumer%20Offset%20Settings%20tab.png?alt=media)

Use this tab to stop the Kafka consumer when the messaged offset timestamp reaches the input timestamp in this screen. By using this tab and the Kafka offset job, you can read messages from the start offset timestamp to the end offset timestamp. Kafka consumer runs in normal mode if no input is provided on this tab.

| Option               | Description                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Offset timestamp** | Specifies the end timestamp to stop the consumer when the message offset timestamp reaches the input timestamp                 |
| **Timestamp format** | <p>Specifies the timestamps format for the offset.</p><p>When an epoch value is given, the timestamp format is not needed.</p> |
